# Artur Dzido
# Zadanie 2, Lista 1
# (Python 3.13.2)


# Funkcyjna implementacja GCD
def fun_gcd(p, q):
    if p < q:
        return fun_gcd(q, p)
    if q:
        return fun_gcd(q, p % q)
    return p


# Imperatywna implementacja GCD
def imp_gcd(p, q):
    if p < q:
        p, q = q, p
    while q:
        p, q = q, p % q
    return p



# Wypisanie wszystkich liczb względnie
# pierwszych nie większych niż n.

n = 42

# Funkcyjnie
def relatively_prime_numbers(n, i):
    if i >= n:
        return
    if fun_gcd(n, i) == 1:
        print(i, end=' ')
    relatively_prime_numbers(n, i + 1)

relatively_prime_numbers(n, 1)
print()

# Imperatywnie
for i in range(n):
    if imp_gcd(n, i) == 1:
        print(i, end=' ')
print()