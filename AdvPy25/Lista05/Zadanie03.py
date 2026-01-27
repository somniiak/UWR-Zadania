import re
import os
import json
from collections import Counter
import requests as r
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

# Zawartość zebranych stron
pages_cached = {}

# Przefiltrowane słowa na stronach
pages_words = {}

def get_page(url):
    '''Pobranie zawartości strony i zapis do pages_cached.'''

    def page_data(action='take', content=None):
        '''Obsługa wczytywania i zapisywania do pliku cache'''
        # Wczytanie danych z pliku
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

        match action:
            case 'take':
                return data.get(url)
            case 'save':
                if url and content:
                    data[url] = content
                    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=4)

    # Zawartość strony została już wczytana
    if url in pages_cached:
        return

    # Sprawdzamy czy już wcześniej zapisaliśmy stronę
    content = page_data('take')
    if content:
        print(f"{url}: Cached data found...")
        pages_cached[url] = content
        get_words(url)
        return

    try:
        with r.get(url, timeout=10) as page:
            status = page.status_code
            status_type = (page.status_code // 100) % 10

            match status_type:
                case 4:
                    print(f"{url}: Client error! ({status})")
                    return
                case 3:
                    print(f"{url}: Redirection... ({status})")
                    return
                case _:
                    print(f"{url}: Downloading... ({status})")

    except r.exceptions.Timeout:
        print(f"{url}: Timed out!")
        return
    
    except r.exceptions.ConnectionError:
        print(f"{url}: Connection error!")
        return

    # Sformatowanie zawartości strony
    content = bs(page.content, features="lxml"
        ).get_text().lower()

    # Zapisanie zawartości
    pages_cached[url] = content

    # Eksport zawartości do pliku cache
    page_data('save', content)

    # Filtrowanie słów
    get_words(url)


def get_words(url):
    '''Przefiltrowanie słów i zapisy do pages_words jako obiekt Counter.'''
    content = pages_cached[url]

    if content:
        pages_words[url] = Counter(
            re.findall(r'[a-zA-Z]{2,}(?!.\.\w{1,3})', content)
        )


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


for url in urls:
    get_page(url)

print(find_most_common(5))
print(find_on_pages("ago"))
