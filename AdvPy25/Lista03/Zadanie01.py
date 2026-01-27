from math import sqrt
from math import floor
from timeit import timeit

# https://pl.wikipedia.org/wiki/Sito_Eratostenesa
# Sito Eratostenesa
# Wyznaczanie liczb pierwszych z przedziału [2; n]

def pierwsze_imperatywna(n):
    if n <= 1:
        return []

    tmp = [True] * (n + 1)
    tmp[0:2] = [False, False]

    for i in range(2, floor(sqrt(n)) + 1):
        if tmp[i]:
            for j in range(i * i, n + 1, i):
                tmp[j] = False

    res = []
    for i in range(n + 1):
        if tmp[i]:
            res.append(i)
    return res

def pierwsze_skladana(n):
    return [i for i in range(2, n + 1) if
        all(i % j for j in range(2, floor(sqrt(i)) + 1))]

def pierwsze_funkcyjna(n):
    return list(filter(lambda num: 
                      all(num % i != 0 for i in range(2, floor(sqrt(num)) + 1)), 
                      list(range(2, n + 1))))

print(f"{'n':>3}\t{'skladana':>10}\t{'imperatywna':>10}\t{'funkcyjna':>10}")
for i in range(20, 200 + 1, 20):
    print(
        f'{i:>3}:\t' +
        f'{timeit(lambda: pierwsze_skladana(i), number=i)*1000:>10.3f}\t' +
        f'{timeit(lambda: pierwsze_imperatywna(i), number=i)*1000:>10.3f}\t' +
        f'{timeit(lambda: pierwsze_funkcyjna(i), number=i)*1000:>10.3f}'
    )