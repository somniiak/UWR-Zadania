import math
from statistics import NormalDist
from scipy.stats import t, f

data1 = []
data2 = []

with open('z1209.csv', 'r') as file:
    temp = [[float(y) for y in x.strip().split(',')] for x in file.readlines()]
    data1 = [x[0] for x in temp]
    data2 = [x[1] for x in temp]

n1 = len(data1)
n2 = len(data2)

avg1 = sum(data1) / n1
avg2 = sum(data2) / n2

s1sqr = sum([(x - avg1)**2 for x in data1]) / n1
s2sqr = sum([(x - avg2)**2 for x in data2]) / n2

print('AvgX1:', avg1)
print('AvgX2:', avg2)
print()

# Podpunkt a)
stat_a = (avg1 - avg2) / math.sqrt(s1sqr**2 / n1 + s2sqr*2 / n2)
res_a = 1 - NormalDist(0, 1).cdf(stat_a)
print('a)', res_a)


# Podpunkt b)
sPsqr = (n1 - 1) * s1sqr + (n2 - 1) * s2sqr
sPsqr /= n1 + n2 -2

stat_b = avg1 - avg2
stat_b /= math.sqrt(sPsqr * ((1 / n1) + (1 / n2)))

res_b = 1 - t.cdf(stat_b, n1 + n2 - 2)
print('b)', res_b)


# Podpunkt c)
stat_c = s1sqr / s2sqr
res_c = 1 - f.cdf(stat_c, n1, n2)
print('c)', res_c)


# Podpunkt d)
stat_d = (n1 * s1sqr) / (n1 - 1)
stat_d /= (n2 * s2sqr) / (n2 - 1)

res_d = 1 - f.cdf(stat_d, n1 - 1, n2 - 1)
print('d)', res_d)
