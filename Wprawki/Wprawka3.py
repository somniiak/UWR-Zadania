def dzielniki(n):
    res = 0
    i = 1
    g = int(n ** 0.5) + 1
    if n == 1:
        return 1
    for i in range(1, g):
        if not n % i:
            res += 1
    if (g - 1) ** 2 == n:
        return (res * 2) - 1
    return res * 2

def zlicz_liczby_dzielnikow(n):
    arr = []
    for i in range(1, n + 1):
        arr.append(dzielniki(i))
    return [(i, arr.count(i)) for i in set(arr)]

n = zlicz_liczby_dzielnikow(3*10**5)
print(n)
