def szachownica(n, k):
    m = n
    n = 2 * n
    while n > 0:
        if n % 2 == 0:
            for i in range(k):
                   print((' ' * k + '#' * k) * m)
            n -= 1
        else:
            for i in range(k):
                    print(('#' * k + ' ' * k) * m)
            n -= 1

szachownica(4, 3)