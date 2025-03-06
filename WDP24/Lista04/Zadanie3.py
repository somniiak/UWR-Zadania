from random import randrange

def randperm(n):
    arr = list(range(n))
    for i in range(n - 1):
        j = randrange(i, n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

for i in range(10):
    print(f'Permutacje {i}:')
    for j in range(5):
        print('\t', randperm(i))

x = randperm(10 ** 6)
#print(x)