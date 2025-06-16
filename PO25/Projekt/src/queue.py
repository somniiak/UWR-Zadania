class QueueManager:
    """Zarządzanie kolejką utworów."""
    def __init__(self):
        self.queue = []
        self.current_index = -1
    
    def add_track(self, video_id):
        """Dodaj utwór do kolejki."""
        if video_id not in self.queue:
            self.queue.append(video_id)
    
    def add_tracks(self, video_ids):
        """Dodaj wiele utworów do kolejki."""
        for video_id in video_ids:
            self.add_track(video_id)
    
    def play_track(self, video_id):
        """Odtwórz konkretny utwór i ustaw go jako aktualny."""
        if video_id in self.queue:
            self.current_index = self.queue.index(video_id)
        else:
            # Jeśli utwór nie jest w kolejce, dodajemy go na początku
            self.queue.insert(0, video_id)
            self.current_index = 0
    
    def next_track(self):
        """Przejdź do następnego utworu."""
        if self.current_index < len(self.queue) - 1:
            self.current_index += 1
            return self.queue[self.current_index]
        return 0
    
    def previous_track(self):
        """Przejdź do poprzedniego utworu."""
        if self.current_index > 0:
            self.current_index -= 1
            return self.queue[self.current_index]
        return 0
    
    def remove_track(self, index):
        """Usuń utwór z kolejki."""
        if 0 <= index < len(self.queue):
            removed = self.queue.pop(index)
            if index < self.current_index:
                self.current_index -= 1
            elif index == self.current_index and self.current_index >= len(self.queue):
                self.current_index = len(self.queue) - 1
            return removed
        return 0

    def clear_queue(self):
        """Wyczyść kolejkę."""
        # Zostaje tylko obecny utwór.
        self.queue = self.queue[self.current_index:self.current_index + 1]
        self.current_index = 0
    
    def get_queue_info(self):
        """Pobierz informacje o kolejce."""
        return {
            'total': len(self.queue),
            'current': self.current_index + 1 if self.current_index >= 0 else 0,
            'has_next': self.current_index < len(self.queue) - 1,
            'has_previous': self.current_index > 0
        }
