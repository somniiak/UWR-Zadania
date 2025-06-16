import os
import asyncio
from textual.app import App
from textual.containers import Container, Vertical, Horizontal
from textual.widgets import Input, DataTable, LoadingIndicator
from textual.widgets import Static, Label, ProgressBar, Button, Footer
from textual_image.widget import Image
from src.queue import QueueManager
from src.audio import AudioServer, format_duration
from src.youtube import YoutubeVideo, youtube_search


class PlayerProgress(Static):
    """Pasek postępu i czas utworu."""
    def compose(self):
        with Horizontal(id="seek_bar"):
            yield Static("0:00", id="track_current_time")
            yield ProgressBar(total=None, show_eta=False, show_percentage=False, id="progress_bar")
            yield Static("0:00", id="track_total_time")

    def on_mount(self):
        self.current_time = self.query_one("#track_current_time", Static)
        self.progress_bar = self.query_one("#progress_bar", ProgressBar)
        self.total_time = self.query_one("#track_total_time", Static)
        self.set_interval(0.1, self.update_progress)

    def update_track_info(self):
        """Aktualizacja informacji o utworze."""
        # Pobranie długości utworu
        self.duration = audio_server.track_duration
        # Aktualizacja czasu utworu
        self.total_time.update(format_duration(self.duration))
        # Aktualizacja paska postępu
        self.progress_bar.update(total=self.duration)

    async def update_progress(self):
        """Aktualizacja paska postępu i czasu."""
        # Sprawdzenie czy utwór się zakończył
        if audio_server.has_finished() and not audio_server.is_paused:
            self.update_track_info()
            await self.app.handle_track_finished()

        # Aktualizacja paska postępu
        self.progress_bar.update(
            progress=audio_server.playback_position()
        )

        # Aktualizacja czasu (HH:MM:SS)
        self.current_time.update(
            format_duration(
                audio_server.playback_position()
            )
        )


class PlayerControls(Static):
    """Przyciski sterujące utworem."""
    def compose(self):
        with Horizontal(id="player_buttons"):
            yield Button("|<", compact=True, id="previous_track_button")
            yield Button("||", compact=True, id="toggle_playback_button")
            yield Button(">|", compact=True, id="next_track_button")

    def on_mount(self):
        self.previous_track_button = self.query_one("#previous_track_button", Button)
        self.toggle_button = self.query_one("#toggle_playback_button", Button)
        self.next_track_button =self.query_one("#next_track_button", Button)

    def update_button_states(self):
        """Aktualizuj stan przycisków na podstawie kolejki."""
        queue_info = queue_manager.get_queue_info()
        self.previous_track_button.disabled = not queue_info['has_previous']
        self.next_track_button.disabled = not queue_info['has_next']

    async def on_button_pressed(self, event: Button.Pressed):
        """Obsłuda przycisków sterujących."""
        match event.button.id:
            case "previous_track_button":
                await self.app.play_previous_track()
            case "toggle_playback_button":
                if audio_server.is_paused:
                    audio_server.unpause_playback()
                    self.toggle_button.label = "||"
                elif audio_server.is_stopped:
                    self.toggle_button.label = "||"
                    audio_server.unpause_playback()
                else:
                    self.toggle_button.label = "|>"
                    audio_server.pause_playback()
            case "next_track_button":
                await self.app.play_next_track()


class PlayerMenu(Container):
    """Menu odtwarzacza."""
    def compose(self):
        with Horizontal(id="player_layout"):
            yield Image(id="album_art")
            with Vertical(id="player_info"):
                yield Label("N/A", id="title_label")
                yield Label("N/A", id="channel_label")
                yield PlayerProgress(id="player_progress")
                yield PlayerControls(id="player_controls")
            with Vertical(id="queue_placeholder"):
                yield QueueInfo(id="queue_info")

    def on_mount(self):
        self.album_art = self.query_one("#album_art", Image)
        self.title_label = self.query_one("#title_label", Label)
        self.channel_label = self.query_one("#channel_label", Label)
        self.player_progress = self.query_one("#player_progress", PlayerProgress)
        self.player_controls = self.query_one("#player_controls", PlayerControls)
        self.queue_info = self.query_one("#queue_info", QueueInfo)
        self.update()

    def update(self):
        self.album_art.image = audio_server.track_cover
        self.title_label.update(audio_server.track_title)
        self.channel_label.update(audio_server.track_channel)
        self.player_progress.update_track_info()
        self.player_controls.update_button_states()
        self.queue_info.update_queue_info()


class PlayerLoader(Container):
    """Menu ładowania przy pobieraniu utworu."""
    def compose(self):
        with Horizontal(id="player_layout"):
            with Vertical(id="player_info"):
                yield Label("Fetching...", id="download_label")
                yield ProgressBar(total=None, show_eta=False, show_percentage=False, id="download_spinner")

    def on_mount(self):
        self.download_label = self.query_one("#download_label", Label)
        self.download_spinner = self.query_one("#download_spinner", ProgressBar)
        self.set_interval(0.01, self.update_progress)

    def update_progress(self):
        self.download_label.update(YoutubeVideo.progress_status)


class QueueInfo(Static):
    """Informacje o kolejce."""
    def compose(self):
        with Vertical(id="queue_info"):
            yield Static("Queue: 0/0", id="queue_status")
            yield Button("Clear", compact=True, id="clear_queue_button")
            yield Button("Remove", compact=True, id="remove_queue_button")

    def on_mount(self):
        self.queue_status = self.query_one("#queue_status", Static)
        self.clear_button = self.query_one("#clear_queue_button", Button)
        self.remove_button = self.query_one("#remove_queue_button", Button)
        self.update_queue_info()

    def update_queue_info(self):
        """Aktualizacja informacji o kolejce."""
        info = queue_manager.get_queue_info()
        self.queue_status.update(f"Queue: {info['current']}/{info['total']}")

    async def on_button_pressed(self, event: Button.Pressed):
        """Obsługa przycisków do zarządzanie kolejką."""
        if event.button.id == "clear_queue_button":
            queue_manager.clear_queue()
            self.update_queue_info()
            self.app.notify("Queue cleared", severity="information")
        
        elif event.button.id == "remove_queue_button":
            queue_info = queue_manager.get_queue_info()
            current_index = queue_manager.current_index
            removed_track = queue_manager.remove_track(current_index)
            
            if removed_track:
                self.app.notify("Removed from queue", severity="information")
                new_queue_info = queue_manager.get_queue_info()
                
                if new_queue_info['total'] == 0:
                    # Nie ma więcej utworów
                    audio_server.stop_playback()
                    if self.app.player_menu.is_mounted:
                        self.app.player_menu.display = False
                    self.app.notify("Queue is empty", severity="information")
                
                elif queue_manager.current_index < new_queue_info['total']:
                    # Następny utwór - teraz ma ten sam indeks
                    next_id = queue_manager.queue[queue_manager.current_index]
                    await self.app.initialize_player(next_id)
                
                elif queue_manager.current_index > 0:
                    # Usunięto ostatni utwór - odtwarzanie poprzedniego
                    queue_manager.current_index -= 1
                    prev_id = queue_manager.queue[queue_manager.current_index]
                    await self.app.initialize_player(prev_id)
                
                else:
                    audio_server.stop_playback()
                    if self.app.player_menu.is_mounted:
                        self.app.player_menu.display = False

                self.update_queue_info()
                if self.app.player_menu.is_mounted:
                    self.app.player_menu.update()

            else:
                self.app.notify("Nothing to remove. This shouldn't happen.", severity="warning")


class SearchScreen(App):
    """Menu głowne aplikacji."""
    # Wczytanie stylów widżetów
    CSS_PATH = "src/styles.tcss"

    # Skróty klawiszowe
    BINDINGS = [
        ("space", "toggle_playback", "Pause/Unpase"),
        ("ctrl+a", "add_all_to_queue", "Add all to queue"),
        ("a", "add_to_queue", "Add to queue"),
        ("n", "next_track", "Next track"),
        ("p", "previous_track", "Previous track"),
    ]

    def compose(self):
        yield Input(placeholder="Search YouTube Music", compact=True, id="search_bar")
        yield Footer(id="screen_footer")

    def on_mount(self):
        self.theme = "dracula"
        self.search_bar = self.query_one("#search_bar", Input)
        self.screen_footer = self.query_one("#screen_footer", Footer)
        self.video_list = DataTable(cursor_type="row", zebra_stripes=True, id="video_list")
        self.video_list.add_columns("Title", "Uploader", "Duration", "ID")
        self.player_menu = PlayerMenu(id="player_menu")
        self.player_loader = PlayerLoader(id="player_loader")
        self.loading_indicator = LoadingIndicator(id="loading_indicator")

    async def on_input_submitted(self, event: Input.Submitted):
        """Obsługa wyszukiwania."""
        query = event.value

        if not self.video_list.is_mounted:
            self.mount(self.video_list, before=self.search_bar)
        if not self.loading_indicator.is_mounted:
            self.mount(self.loading_indicator, before=self.search_bar)

        self.video_list.display = False
        self.loading_indicator.display = True

        try:
            videos = await youtube_search(query)

            self.video_list.clear()
            for video in videos:
                if len(video['id']) != 11:
                    continue

                self.video_list.add_row(
                    video.get("title", "N/A"),
                    video.get("channel", "N/A"),
                    format_duration(video.get("duration", "0.0")),
                    video.get("id", "N/A"),
                )

            self.loading_indicator.display = False
            self.video_list.display = True
            self.video_list.focus()

        except Exception as e:
            self.notify(f"Search failed: {str(e)}", severity="error")
            if self.loading_indicator.is_mounted:
                self.loading_indicator.remove()

    async def on_data_table_row_selected(self, event: DataTable.RowSelected):
        """Obsługa wybrania utworu."""
        # Pobranie id filmu wybranego wiersza
        cursor_row = event.data_table.cursor_row
        selected_row = event.data_table.get_row_at(cursor_row)
        video_id = selected_row[-1]
        await self.initialize_player(video_id)

    def action_toggle_playback(self):
        """Przycisk pauzy."""
        if self.player_menu.is_mounted:
            self.player_menu.player_controls.toggle_button.action_press()

    async def action_next_track(self):
        """Przejście do następnego utworu."""
        await self.play_next_track()

    async def action_previous_track(self):
        """Przejście do poprzedniego utworu."""
        await self.play_previous_track()

    def action_add_to_queue(self):
        """Dodanie zaznaczonego utwór do kolejki."""
        if self.video_list.is_mounted and self.video_list.cursor_row is not None:
            cursor_row = self.video_list.cursor_row
            selected_row = self.video_list.get_row_at(cursor_row)
            video_id = selected_row[-1]
            queue_manager.add_track(video_id)
            self.notify(f"Added to queue: {selected_row[0]}", severity="information")
            if self.player_menu.is_mounted:
                self.player_menu.update()

    def action_add_all_to_queue(self):
        """Dodanie wszystkich utworów z wyszukiwania do kolejki."""
        if self.video_list.is_mounted:
            video_ids = []
            for row_key in self.video_list.rows:
                row = self.video_list.get_row(row_key)
                video_ids.append(row[-1])
            queue_manager.add_tracks(video_ids)
            self.notify(f"Added {len(video_ids)} tracks to queue", severity="information")
            if self.player_menu.is_mounted:
                self.player_menu.update()

    async def play_next_track(self):
        """Odtworzenie następnego utwóru z kolejki."""
        next_id = queue_manager.next_track()
        if next_id:
            await self.initialize_player(next_id)
        else:
            self.notify("No next track in queue", severity="warning")

    async def play_previous_track(self):
        """Odtworzenie poprzedniego utwóru z kolejki."""
        prev_id = queue_manager.previous_track()
        if prev_id:
            await self.initialize_player(prev_id)
        else:
            self.notify("No previous track in queue", severity="warning")

    async def handle_track_finished(self):
        """Obsługa zakończenia utworu, przejście do następnego."""
        if queue_manager.get_queue_info()['has_next']:
            await self.play_next_track()

    async def initialize_player(self, video_id):
        """Odtwarzanie wybranego utworu."""
        track = YoutubeVideo(video_id)
        audio_server.stop_playback()
        queue_manager.play_track(video_id)

        if self.player_menu.is_mounted:
            self.player_menu.display = False
        if not self.player_loader.is_mounted:
            self.mount(self.player_loader, before=self.video_list)

        self.player_loader.display = True

        await asyncio.gather(
            track.download_thumbnail(),
            track.download_audio()
        )

        self.player_loader.display = False
        self.player_menu.display = True

        audio_server.init_track(video_id)
        audio_server.play_track()

        if self.player_menu.is_mounted:
            self.player_menu.update()
        else:
            self.mount(self.player_menu, before=self.video_list)


if __name__ == "__main__":
    os.makedirs(".temp", exist_ok=True)
    audio_server = AudioServer()
    audio_server.init_pygame()
    queue_manager = QueueManager()
    app = SearchScreen()
    app.run()
