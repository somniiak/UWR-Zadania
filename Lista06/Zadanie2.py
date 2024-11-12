with open('popularne_slowa2023.txt', 'r') as f:
    slowa = set(i.strip() for i in f.readlines())
odwrotne_slowa = set(slowo[::-1] for slowo in slowa)

# Elementy wspólne zbiorów
res = list(slowa & odwrotne_slowa)
# Usuwanie palindromów np. 'a', 'menem', ...
# i poprawne sformatowanie wyniku np. 'latem-metal', ...
res = [f'{i}-{i[::-1]}' for i in res if i != i[::-1]]
print(sorted(res))