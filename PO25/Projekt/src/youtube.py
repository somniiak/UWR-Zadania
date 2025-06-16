import os
import asyncio
from io import BytesIO
import concurrent.futures
import yt_dlp
import requests
from PIL import Image
from src.database import VideoDatabase

class YoutubeVideo:
    """Pobieranie zasobów i danych utworu."""
    progress_status = "Fetching..."

    def __init__(self, video_id):
        self.video_id = video_id
        self.video_url = 'https://youtube.com/watch?v=' + video_id
        self.thumbnail_url = 'https://i.ytimg.com/vi/' + video_id + '/sddefault.jpg'
        self.output_path = os.path.join(".temp", f"{self.video_id}.ogg")
        self.thumbnail_path = os.path.join(".temp", f"{self.video_id}.jpg")


    async def download_thumbnail(self):
        """Pobranie i konwersja okładki."""
        def _get_thumbnail():
            if not os.path.exists(self.thumbnail_path):
                response = requests.get(self.thumbnail_url, timeout=10)
                with BytesIO(response.content) as img_data:
                    with Image.open(img_data) as img:
                        img = img.crop((140, 60, 500, 420))
                        img.save(self.thumbnail_path)

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, _get_thumbnail)


    async def download_audio(self):
        """Pobieranie i konwersja pliku audio."""
        def _get_audio():
            def progress_hook(d):
                if d['status'] == 'downloading':
                    YoutubeVideo.progress_status = "Downloading video..."
                elif d['status'] == 'started':
                    YoutubeVideo.progress_status = "Processing video..."

            yt_dlp_opts = {
                'format': 'bestaudio',
                'quiet': True,
                'noplaylist': True,
                'outtmpl': f".temp/{self.video_id}",
                'progress_hooks': [progress_hook],
                'postprocessor_hooks': [progress_hook],
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'vorbis',
                    'preferredquality': '64',
                }],
            }

            if not os.path.exists(self.output_path):
                with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
                    ydl.download(self.video_url)
                YoutubeVideo.progress_status = "Fetching..."

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, _get_audio)


async def youtube_search(query, max_results=40):
    """Wyszukiwanie utworów i zapis do bazy danych."""
    def _search():
        yt_dlp_opts = {
            'quiet': True,
            'skip_download': True,
            'extract_flat': True,
        }
        with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl:
            search_url = f"ytsearch{max_results}:{query}"
            entries = ydl.extract_info(search_url, download=False)['entries']

        for entry in entries:
            if entry.get('id'):
                VideoDatabase.add(
                    entry.get("id", "N/A"),
                    entry.get("title", "N/A"),
                    entry.get("channel", "N/A"),
                    entry.get("duration", 0.0),
                )

        return entries

    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        return await loop.run_in_executor(executor, _search)
