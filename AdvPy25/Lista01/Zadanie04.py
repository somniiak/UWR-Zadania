from random import random
from math import pi

# Wymiary tarczy
n = 100

# Promień okręgu
r = n / 2

# Zmienne
ltwo = 0
cltwt = 0

# Czy trafiono okrąg
def hit_target(xn, yn):
    return xn ** 2 + yn ** 2 <= r ** 2

# Losowanie pozycji
def get_random_pos():
    return n * (random() - 0.5)

# Zadana liczba losowań
def pi_iter(tries):
    global ltwo, cltwt
    for _ in range(tries):
        rnd_x = get_random_pos()
        rnd_y = get_random_pos()

        if hit_target(rnd_x, rnd_y):
            ltwo += 1
        cltwt += 1

# Różnica między przybliżeniem
def pi_approx(epsilon):
    global ltwo, cltwt
    while True:
        rnd_x = get_random_pos()
        rnd_y = get_random_pos()

        if hit_target(rnd_x, rnd_y):
            ltwo += 1
        cltwt += 1

        if abs(pi - 4 * ltwo / cltwt) < epsilon:
            break

#pi_iter(999999)
pi_approx(0.00000001)
print('ltwo:', ltwo, 'cltwt:', cltwt, 'π ≈', 4 * ltwo / cltwt)