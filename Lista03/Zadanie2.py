import itertools
import math

def isPrime(n):
    while n > 1:
        # Optymalizacja funkcji: od N to sqrt(N)
        # zamiast (N // 2) + 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

# n - liczba siódemek
# m - długość liczby
n = 7
m = 10

# Grupy (m - n) liczb do wypełnienia miejsc
# poza siódemkami w następnych obliczeniach.
# Zastosowana optymalizacja polega na usunięciu
# zestawów zawierających te same liczby bo w
# permutacjach wyjdzie i tak to samo.
nums = set([''.join(sorted(i)) for i in itertools.product('0123456789', repeat=(m - n))])
nums = [list(i) for i in nums]

# Permutacje (m - n) liczb z n siódemkami
# np. ['3, '5', '2', '7777777']
results = []
for num in nums:
    num.append('7' * n)
    num = [''.join(i) for i in itertools.permutations(num) if i[0] != '0' and isPrime(int(''.join(i)))]
    for l in num:
        results.append(l)

results = sorted(set(results))
print(results, len(results))
