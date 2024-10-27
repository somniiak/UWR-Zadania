from random import choice

def randperm(n):
    nums = list(range(n))
    nums = [choice(nums) for i in range(n)]
    return nums

for i in range(10):
    print(f'Permutacje {i}:')
    for j in range(3):
        print(f'\t{randperm(i)}')

x = randperm(10 ** 6)
#print(x)