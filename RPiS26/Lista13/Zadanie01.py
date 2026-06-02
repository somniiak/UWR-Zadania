import math
from statistics import NormalDist

datax, datay = [], []

with open('rpr-1301.csv', 'r') as file:
    temp = [[float(y) for y in x.strip().split(',')] for x in file.readlines()]
    datax = [x[0] for x in temp]
    datay = [x[1] for x in temp]

nx = len(datax)
ny = len(datay)

avgx = sum(datax) / nx
avgy = sum(datay) / ny

stat_z = (avgx - avgy) / math.sqrt((4 / nx) + (9 + ny))
cdf_z = NormalDist(0, 1).cdf(stat_z)
val_p = 2 * (1 - cdf_z)
print('CDF: ', cdf_z)
print('p-value: ', val_p)