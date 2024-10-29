import numpy as np

randperm = lambda n : np.random.permutation(np.array(list(range(n)))).tolist()

for i in range(10):
    print(f'Permutacje {i}:')
    for j in range(3):
        print(f'\t{randperm(i)}')

x = randperm(10 ** 6)
#print(x)