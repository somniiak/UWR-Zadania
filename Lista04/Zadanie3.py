from itertools import permutations
from itertools import product
from random import choice

def randperm(n):
    nums = '0123456789'
    if n <= 9:
        nums = nums[:n]
    print(nums)
    #nums = [''.join(i) for i in permutations(nums, n)]
    nums = [i for i in product(nums, repeat=n)]
    #return choice(nums)
    return nums

x = randperm(13)
print(x)

'''
for i in range(10):
    print(f'Permutacje {i}:')
    for j in range(3):
        print(f'\t{randperm(i)}')
'''