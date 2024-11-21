from murek import *
from random import randint

speed('fastest')
for _ in range(4):
    for _ in range(10):
        p = str(randint(1, 6))
        murek(p, 20)
        murek('f', 20)
    murek('r', 20)


# Liczba pasków z kwadratów
n = 19

tracer(2)
speed('fastest')
boki = list(range(2, n + 1))

sq_sides(n)
for bok in boki:
    murek('fc' * bok + 'r', 25)
input()