from time import time

def sudan(n, x, y):
    if n == 0:
        return x + y
    if y == 0:
        return x
    return sudan(n - 1, sudan(n, x, y - 1), sudan(n, x, y - 1) + y)

def sudan_memo(n, x, y):
    memo = {}

    def aux(n, x, y):
        if (n, x, y) in memo:
            return memo[(n, x, y)]
        elif n == 0:
            res = x + y
        elif y == 0:
            res = x
        else:
            tmp = aux(n, x, y - 1)
            res = aux(n - 1, tmp, tmp + y)
        memo[(n, x, y)] = res
        return res

    return aux(n, x, y)


for x in range(3):
    for y in range(3):
        start = time()
        print(f"sudan_memo(2, {x}, {y}) = " + str(sudan_memo(2, x, y)) + "; ", end = "")
        print(round((time() - start) * 1000, 2))

        start = time()
        print(f"sudan(2, {x}, {y}) = " + str(sudan(2, x, y)) + "; ", end = "")
        print(round((time() - start) * 1000, 2))