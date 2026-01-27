import re
from random import randint
import os
import requests

def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    tekst = re.sub(r"[^\w ]", "", tekst).split(' ')
    tekst = [slowo for slowo in tekst if len(slowo) <= dl_slowa]
    while len(tekst) > liczba_slow:
        del tekst[randint(0, len(tekst) - 1)]
    return " ".join(tekst)


if not os.path.exists("book.txt"):
    url = 'https://wolnelektury.pl/media/book/txt/sklepy-cynamonowe-ulica-krokodyli.txt'

    with requests.get(url) as r:
        with open("book.txt", "w") as f:
            f.write(r.text[:r.text.index('-----')])

with open("book.txt", "r") as f:
    print("".join([uprosc_zdanie(l, 15, 15).capitalize() + "." if l.strip() else l for l in f.readlines()]))