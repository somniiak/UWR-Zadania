import asyncio
from aiohttp import ClientSession
from util import *
from rich import print, box
from rich.table import Table
from rich_pixels import Pixels
from PIL import Image
from io import BytesIO
from private import tmdb_key

class TMDBScrapper():
    def __init__(self):
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {tmdb_key}"
        }

    async def __aenter__(self):
        self.session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    def get_url(self, video_id):
        return f'https://api.themoviedb.org/3/movie/{video_id}'

    async def get_image(self, path: str):
        url = f"https://image.tmdb.org/t/p/w200{path}"
        async with self.session.get(url) as r:
            data = await r.read()
            img = Image.open(BytesIO(data))
            return img.resize((30, 40))

    async def get_video(self, video_id):
        async with self.session.get(self.get_url(video_id), headers=self.headers) as r:
            body = await r.json()
            body['poster'] = await self.get_image(body.get("poster_path"))
            return body

    async def draw_table(self, *video_ids):
        queue = [self.get_video(video_id) for video_id in video_ids]
        videos = await asyncio.gather(*queue)

        table = Table()
        table.add_column('TheMovieDB', justify='center')

        for video in videos:
            video_table = Table(
                show_lines=True,
                box=box.ROUNDED
            )

            video_table.add_column("Poster", width=30, justify="center")
            video_table.add_column("Details", justify="left")

            video_table.add_row(
                Pixels.from_image(video.get('poster')),
                f'[bright_yellow bold]{video.get("title")}[/bright_yellow bold]\n\n' +
                f'[bright_black italic]{video.get('tagline')}[/bright_black italic]\n\n' +
                f'{video.get('overview')}'
            )

            table.add_row(video_table)

        console.print(table)
