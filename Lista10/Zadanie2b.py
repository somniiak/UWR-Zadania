from collections import defaultdict as dd

alpha = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
len_alpha = len(alpha)

def to_num(word):
    res = []
    for idx in range(len(word) - 1):
        cur = alpha.index(word[idx])
        nxt = alpha.index(word[idx + 1])
        res.append((nxt - cur) % len_alpha)
    return tuple(res)

with open('popularne_slowa2023.txt', 'r') as f:
    words = set(i.strip() for i in f.readlines())

valid = dd(list)
for word in words:
    valid[to_num(word)].append(word)

res = dd(list)
for k, v in valid.items():
    if len(v) >= 2:
        res[len(k) + 1].append(v)

for k, v in sorted(res.items()):
    print(f'{k}: ', end=' ')
    for values in v:
        print(values, end=',')
    print('\n')