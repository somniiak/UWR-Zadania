import os
import requests

def kompresja(s):
    arr = []
    for l in s:
        if arr:
            if arr[-1][1] == l:
                c, p = arr.pop()
                arr.append((c + 1, p))
            else:
                arr.append((1, l))
        else:
            arr.append((1, l))
    return arr

def dekompresja(xs):
    return "".join([x[0] * x[1] for x in xs])


if not os.path.exists("book.txt"):
    url = 'https://wolnelektury.pl/media/book/txt/sklepy-cynamonowe-ulica-krokodyli.txt'

    with requests.get(url) as r:
        with open("book.txt", "w") as f:
            f.write(r.text[:r.text.index('-----')])

with open("book.txt", "r") as f:
    x = "".join(f.readlines())

    x = kompresja(x)
    print(x)

    x = dekompresja(x)
    print(x)