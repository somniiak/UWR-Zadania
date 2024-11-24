from murek import *
from random import randint

# Boki kwadratu:
n = 30
# Długość boku kwadracika
k = 15

i = 0
grid = [['#'] * n] * n
tracer(10)
goto(-n * k // 2, n * k // 2)
speed('fastest')
murek('1f', k)
for rows in grid:
    for items in rows:
        p = str(randint(1, 6))
        murek(p + 'f', k)
    i += 1
    if i % 2:
        murek('rfr', k)
    elif i == n:
        input()
    else:
        murek('lfl', k)