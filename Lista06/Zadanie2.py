with open('popularne_slowa2023.txt', 'r') as f:
    slowa = set(i.strip() for i in f.readlines())
odwrotne_slowa = set(slowo[::-1] for slowo in slowa)

# Elementy wspólne zbiorów
res = list(slowa & odwrotne_slowa)
res = set(tuple(sorted([i, i[::-1]])) for i in res)
res = [f'{i[0]}-{i[1]}' for i in res]
print(sorted(res))
print(len(res))
