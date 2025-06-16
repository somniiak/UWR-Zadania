# Artur Dzido
# Zadanie 1, Lista 1
# (Python 3.13.2)


# Funkcyjna implementacja silni
def fun_silna(n):
    if not n:
        return 1
    return n * fun_silna(n - 1)

# Imperatywna implementacja silni
def imp_silnia(n):
    res = 1
    while n:
        res *= n
        n -= 1
    return res

# Symbol Newtona
def binom(n, k):
    if k > n:
        return
    return imp_silnia(n) // (imp_silnia(k) * imp_silnia(n - k))

# n-ty wiersz trójkąta Pascala
n = 5
for k in range(n):
    print(binom(n - 1, k), end=' ')