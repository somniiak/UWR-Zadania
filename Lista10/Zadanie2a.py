from collections import defaultdict as dd

alpha = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
alpha_len = len(alpha)

shifts = {k: alpha[k:] + alpha[:k] for k in range(1, alpha_len)}

alpha = {char: idx for idx, char in enumerate(alpha)}

caesar = lambda s, k : ''.join([shifts[k % alpha_len][alpha[l]] if l in alpha else l for l in s])

with open('popularne_slowa2023.txt', 'r') as f:
    slowa = set(i.strip() for i in f.readlines())

def caesar_pairs(s):
    res = []
    for k in range(1, alpha_len):
        secret = caesar(s, k)
        if secret in slowa:
            res.append(secret)
    if res:
        res.append(slowo)
        return tuple(sorted(res))
    else:
        return None


valid = dd(lambda: set())
for slowo in slowa:
    secrets = caesar_pairs(slowo)
    if secrets:
        valid[len(slowo)].add(secrets)
print(valid[max(valid.keys())])
