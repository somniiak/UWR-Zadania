import re
import os
import json
import asyncio
from collections import Counter
from aiohttp import ClientSession
from bs4 import BeautifulSoup as bs

# Adresy stron do analizy
urls = [
    "https://soatok.blog/b/",
    "https://torrentfreak.com/",
    "https://news.ycombinator.com/news",
    "https://lobste.rs/",
    "https://lwn.net/",
    "https://www.laws-of-software.com/",
]

# Przygotowanie pliku cache
CACHE_FILE = 'cache.json'

if not os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump({}, f)


def load_cache():
    '''Odczyt danych z pliku cache.'''
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_cache(data):
    '''Zapis danych do pliku cache.'''
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


# Zawartość zebranych stron
pages_cached = load_cache()

# Przefiltrowane słowa na stronach
pages_words = {}


async def get_page(url, session):
    '''Pobranie zawartości strony i zapis do pages_cached.'''

    # Sprawdzamy czy już wcześniej zapisaliśmy stronę
    if url in pages_cached:
        print(f"{url}: Cached data found...")
        return

    try:
        async with session.get(url, timeout=10) as response:

            status = response.status
            if 400 <= status < 500:
                print(f"{url}: Client error! ({status})")
                return
            elif 300 <= status < 400:
                print(f"{url}: Redirection... ({status})")
                return
            else:
                print(f"{url}: Downloading... ({status})")                    

            # Odczytanie zawartości strony
            text = await response.text()

            # Sformatowanie zawartości strony
            content = bs(text, "lxml").get_text().lower()

            # Zapisanie zawartości
            pages_cached[url] = content

    except asyncio.TimeoutError:
        print(f"{url}: Timed out!")
        return

    except Exception as e:
        print(f"{url}: Error: {e}")
        return


def get_words():
    '''Przefiltrowanie słów i zapisy do pages_words jako obiekt Counter.'''
    for url, content in pages_cached.items():
        pages_words[url] = Counter(
            re.findall(r'[a-zA-Z]{2,}(?!.\.\w{1,3})', content))


def find_most_common(count=1):
    '''Najczęsciej występujące słowo(a) na stronach.'''
    # Drugi parametr Counter() jest konieczny jako wyraz
    # wobec którego sumujemy (w.p.p. jest to 0 - błąd!)
    return sum(
            pages_words.values(), Counter()
        ).most_common(count)


def find_on_pages(word):
    '''Strony na których pojawia się zadane słowo.'''
    return [k for k, v in pages_words.items() if word in v]


async def runner():
    '''Asynchroniczne pobieranie stron.'''
    async with ClientSession() as session:
        fetch = [get_page(url, session) for url in urls]
        await asyncio.gather(*fetch)

    # Szukanie słów na stronach
    get_words()

    # Zapis stron do pliku cache
    save_cache(pages_cached)


# Przygotowanie pobierania
asyncio.run(runner())

print(find_most_common(5))
print(find_on_pages("blog"))
