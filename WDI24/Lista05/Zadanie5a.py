def fTrec(n, m):
    if not m:
        return n
    elif not n:
        return m
    else:
        return fTrec(n - 1, m) + 2 * fTrec(n, m - 1)

x = fTrec(3, 4)
print(x)