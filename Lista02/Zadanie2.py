def koperta(n):
    n = 2 * n + 1
    k = n - 2
    print('*' * n)
    for i in range(k // 2):
        print('*' + ' ' * i + '*', end='')
        print(' ' * (k - (2 * i) - 2), end='')
        print('*' + ' ' * i + '*', end='')
        print()
    print('*' + ' ' * (i + 1) + '*' + ' ' * (i + 1) + '*')
    for i in range((k // 2) - 1, -1, -1):
        print('*' + ' ' * i + '*', end='')
        print(' ' * (k - (2 * i) - 2), end='')
        print('*' + ' ' * i + '*', end='')
        print()
    print('*' * n)

koperta(4)