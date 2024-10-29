from random import choice
from random import randrange

def randperm(n):
    res = []
    i = n
    nums = list(range(n))
    while len(res) != n:
        res.append(nums.pop(randrange(i)))
        i -= 1
    return res

for i in range(10):
    print(f'Permutacje {i}:')
    for j in range(3):
        print(f'\t{randperm(i)}')

x = randperm(10 ** 6)
print(x)