import sqlite3
import os

class VideoDatabase:
    """Obsługa bazy danych z informacjami o utworach."""
    db_path = os.path.join(".temp", "data.db")
    _initialized = False

    @classmethod
    def _ensure_init(cls):
        """Inicjalizacja bazy danych."""
        if not cls._initialized:
            db_exists = os.path.exists(cls.db_path)
            with sqlite3.connect(cls.db_path) as conn:
                cursor = conn.cursor()
                if not db_exists:
                    cursor.execute('''
                        CREATE TABLE songs (
                            video_id TEXT PRIMARY KEY,
                            title TEXT NOT NULL,
                            channel TEXT NOT NULL,
                            duration REAL NOT NULL
                        )
                    ''')
                    conn.commit()
            cls._initialized = True
    
    @classmethod
    def add(cls, video_id, title, channel, duration):
        """Dodane danych do bazy."""
        cls._ensure_init()
        with sqlite3.connect(cls.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT video_id FROM songs WHERE video_id = ?",
                (video_id,)
                )
            if not cursor.fetchone():
                cursor.execute(
                    "INSERT INTO songs (video_id, title, channel, duration) VALUES (?, ?, ?, ?)",
                    (video_id, title, channel, duration)
                )
            conn.commit()

    @classmethod
    def get(cls, video_id):
        """Pobranie danych z bazy."""
        cls._ensure_init()
        with sqlite3.connect(cls.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT video_id, title, channel, duration FROM songs WHERE video_id = ?", 
                (video_id,)
            )
            result = cursor.fetchone()

        if result:
            return {
                "video_id": result[0],
                "title": result[1],
                "channel": result[2],
                "duration": result[3]
            }

        else:
            raise LookupError(f"Song with video_id {video_id} not found.")
