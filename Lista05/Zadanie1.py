from statistics import mean
from statistics import median


def F(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def energia(n):
    i = n
    j = 0
    while i != 1:
        i = F(i)
        j += 1
    return j

def pretty_print(arr):
    print(arr)
    print('Średnia:', mean(arr))
    print('Mediana:', median(arr))
    print('Min/Max:', min(arr), max(arr))

def analiza_collatza(a, b):
    if a > b:
        a, b = b, a
    arr = [energia(i) for i in range(a, a + b)]
    pretty_print(arr)


analiza_collatza(1, 5)