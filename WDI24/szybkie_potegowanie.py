# Wersja iteracyjna:
# Pamięć:   O(1)
# Czas:     O(log(b))
def potIter(a, b):
    rez = 1
    while b > 0:
        if b % 2:
            rez = rez * a
        b = b // 2
        a = a * a
    return rez

# Wersja rekurencyjna:
# Pamięć:   O(log(b))
# Czas:     O(log(b))
def potRec(a, b):
    if not b:
        return 1
    if b % 2:
        return a * potRec(a * a, b // 2)
    return potRec(a * a, b // 2)