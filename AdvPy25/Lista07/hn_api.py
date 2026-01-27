import asyncio
from aiohttp import ClientSession
from util import *
from rich import print, box
from rich.table import Table

class HNPost():
    def __init__(self, **post_data):
        self.data = {
            'id': post_data.get('id', ''),
            'author': post_data.get('by', ''),
            'title': post_data.get('title', ''),
            'text': post_data.get('text'),
            'kids': post_data.get('kids', []),
        }

        self.comments = []

    def add_comments(self, *comments):
        for comment in comments:
            self.comments.append(comment)
    
    def get_table(self):
        table = Table(
            title=str(self.data['id']),
            expand=True,
            show_lines=True,
            box=box.ROUNDED
        )

        table.add_column(self.data['author'])
        table.add_column(self.data['title'])
        
        if self.data['text']:
            table.add_row('', decode(self.data['text']))

        for comment in self.comments:
            if not comment.data['deleted']:
                table.add_row(
                    f'[yellow italic]{comment.data['author']}[/yellow italic]',
                    decode(comment.data['text']),
                )
        
        return table


class HNComment():
    def __init__(self, **comment_data):
        if comment_data.get('type') != 'comment':
            raise ValueError('Invalid type: not a comment.')
        
        self.data = {
            'author': comment_data.get('by', ''),
            'text': comment_data.get('text', ''),
            'deleted': comment_data.get('deleted', False)
        }

class HNScrapper():
    def __init__(self):
        self.api_url = 'https://hacker-news.firebaseio.com/v0/'
        self.top_posts = []
        self.saved_posts = {}

    async def __aenter__(self):
        self.session = ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    async def fetch_top(self):
        '''Ściąganie najpopularniejszych postów.'''
        async with self.session.get(self.api_url + 'topstories.json') as r:
            self.top_posts = await r.json()

    async def get_top(self, count):
        '''Zwraca określoną liczbę najpopularniejszych postów.'''
        if not self.top_posts:
            await self.fetch_top()
        return self.top_posts[:count]
    
    async def fetch_post(self, post_id):
        '''Ściąganie danych posta'''
        async with self.session.get(self.api_url + 'item/' + str(post_id) + '.json') as r:
            return await r.json()

    async def get_post(self, comment_count, post_id):
        '''Zapisanie danych posta z określoną liczbą komentarzy.'''
        if post_id not in self.saved_posts:
            post_data = await self.fetch_post(post_id)
            post = HNPost(**post_data)

            # Asynchroniczne ściąganie komentarzy do posta
            queue = [self.fetch_post(kid_id) for kid_id in post.data['kids'][:comment_count]]
            comments_data = await asyncio.gather(*queue)

            # Zapakowanie komentarzy do odpowiedniej klasy
            post.add_comments(*[HNComment(**kid) for kid in comments_data])

            self.saved_posts[post_id] = post

    async def draw_table(self, comment_count, *post_ids):
        '''Wypisanie tabelki złożonej z tabelek postów.'''

        # Ściągamy niezapisane posty
        queue = [self.get_post(comment_count, post_id) for post_id in post_ids if post_id not in self.saved_posts]
        await asyncio.gather(*queue)
        
        # Tabelka tabelek
        table = Table()
        table.add_column('Hacker News', justify='center')

        for post in self.saved_posts.values():
            table.add_row(post.get_table())

        console.print(table)