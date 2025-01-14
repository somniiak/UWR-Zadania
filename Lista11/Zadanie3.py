from collections import Counter

with open('wyniki.txt', 'r', encoding='utf-8-sig') as f:
    lines = [i.strip().split(',') for i in f.readlines()]
    lines = [(i[0], int(i[1])) for i in lines]

M = 460 # Liczba mandatów do rozdzielenia
N = len(lines) # Lizcba komitetów

quot = []
for line in lines:
    party, votes = line
    for n in range(1, M + 1):
        quot.append((votes / n, party))

quot = sorted(quot, reverse=True)[:M]
results = Counter([v[1] for v in quot])
print(results)