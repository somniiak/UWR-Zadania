import asyncio
from hn_api import HNScrapper
from tmdb_api import TMDBScrapper

async def hn_runner():
    async with HNScrapper() as scrapper:
        top_posts = await scrapper.get_top(2)
        await scrapper.draw_table(1, *top_posts)

async def tmdb_runner():
    async with TMDBScrapper() as scrapper:
        posts = [
            '269149',
            '1084242',
            '1923',
        ]
        await scrapper.draw_table(*posts)

asyncio.run(hn_runner())
asyncio.run(tmdb_runner())