import math

data = []

with open('z1210.csv', 'r') as f:
    data = [float(x) for x in f.readlines()]


# Podpunkt a)
box_muller = [
    (
        math.sqrt(-2 * math.log(x)) * math.cos(2 * math.pi * y),
        math.sqrt(-2 * math.log(x)) * math.sin(2 * math.pi * y)
    ) for x, y in zip(data[::2], data[1::2])
]

# https://stackoverflow.com/a/10636583
box_muller = list(sum(box_muller, ()))

avg_a = sum(box_muller) / len(box_muller)
s2_a = sum([(x - avg_a)**2 for x in box_muller]) / len(box_muller)

print(f'a) avg = {avg_a}, s2 = {s2_a}')


# Podpunkt b)
inv_cdf_b = lambda u: -0.25 * math.log(1 - u)
data_b = [inv_cdf_b(x) for x in data]

avg_b = sum(data_b) / len(data_b)
s2_b = sum([(x - avg_b)**2 for x in data_b]) / len(data_b)

print(f'b) avg = {avg_b}, s2 = {s2_b}')


# Podpunkt c)
inv_cdf_c = lambda u: 4 * math.sqrt(u)
data_c = [inv_cdf_c(x) for x in data]

avg_c = sum(data_c) / len(data_c)
s2_c = sum([(x - avg_c)**2 for x in data_c]) / len(data_c)

print(f'c) avg = {avg_c}, s2 = {s2_c}')
