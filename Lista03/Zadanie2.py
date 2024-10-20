import itertools

# n - liczba siódemek
# m - długość liczby
n = 7
m = 10


# Grupy (m - n) liczb do wypełnienia miejsc poza
# siódemkami w następnych kombinacjach.
nums = [list(i) for i in itertools.product('0123456789', repeat=(m - n))]

# Permutacje (m - n) liczb z n siódemkami
# np. ['3, '5', '2', '7777777']
results = []
for num in nums:
    num.append('7' * n)
    num = [''.join(i) for i in itertools.permutations(num) if i[0] != '0']
    for l in num:
        results.append(l)

results = sorted(set(results))
print(results, len(results))
