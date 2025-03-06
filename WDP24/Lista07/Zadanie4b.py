from murek import *
from random import randint

# Liczba pasków z kwadratów
n = 19

tracer(2)
speed('fastest')
boki = list(range(2, n + 1))

sq_sides(n)
for bok in boki:
    murek('cf' * bok + 'r', 25)
input()