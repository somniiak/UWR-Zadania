import os
import pygame
from src.database import VideoDatabase


class AudioServer:
    """Klasa zarządzająca odtwarzaniem audio."""
    def init_track(self, video_id):
        """Wczytanie danych utworu."""
        info = VideoDatabase.get(video_id)

        self.track_title = info.get("title", "N/A")
        self.track_channel = info.get("channel", "N/A")
        self.track_duration = info.get("duration", "N/A")

        self.track_path = os.path.join(".temp", f"{video_id}.ogg")
        self.track_cover = os.path.join(".temp", f"{video_id}.jpg")

        self.is_paused = True
        self.is_stopped = True

    def play_track(self):
        """Załadowanie pliku i odtworzenie."""
        self.is_paused = False
        self.is_stopped = False
        pygame.mixer.music.load(self.track_path)
        pygame.mixer.music.rewind()
        pygame.mixer.music.play()

    def init_pygame(self):
        """Pygame do odtwarzania dźwięku."""
        pygame.init()
        pygame.mixer.init()

    def unpause_playback(self):
        """Wznowienie odtwarzania."""
        self.is_paused = False
        pygame.mixer.music.unpause()

    def pause_playback(self):
        """Zatrzymanie odtwarzania."""
        self.is_paused = True
        pygame.mixer.music.pause()

    def stop_playback(self):
        """Zakończenie odtwarzania."""
        self.is_stopped = True
        pygame.mixer.music.rewind()
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def has_finished(self):
        """Status odtwarzania."""
        return not pygame.mixer.music.get_busy()

    def playback_position(self):
        """Zwrócenie obecnej pozycji (sekundy)."""
        return float(pygame.mixer.music.get_pos()) / 1000.0


def format_duration(duration):
    """Formatowanie czasu jako HH:MM:SS"""
    minutes = int(duration // 60)
    seconds = int(duration % 60)
    return f"{minutes}:{seconds:02d}"
