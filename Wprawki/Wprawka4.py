import re
with open('popularne_slowa2023.txt', 'r') as f:
    slowa = list(map(str.strip, f))

slowa_sorted = set(''.join(sorted(slowo)) for slowo in slowa)

dict = {}
for slowo in slowa_sorted:
    dict[slowo] = []

for slowo in slowa:
    sorted_slowo = ''.join(sorted(slowo))
    dict[sorted_slowo].append(slowo)

for k, v in dict.items():
    if len(v) >= 5:
        for slowo in v:
            print(slowo, end=' ')
        print()
