import math
from scipy.stats import t
import numpy as np

datax, datay = [], []

with open('rpr-1302.csv', 'r') as file:
    temp = [[float(y) for y in x.strip().split(',')] for x in file.readlines()]
    datax = [x[0] for x in temp]
    datay = [x[1] for x in temp]

nx = len(datax)
ny = len(datay)

avgx = sum(datax) / nx
avgy = sum(datay) / ny

s2x = np.var(datax, ddof=1)
s2y = np.var(datay, ddof=1)

pooled_var = math.sqrt(((nx - 1) * s2x + (ny - 1) * s2y) / (nx + ny - 2))

stat_z = (avgx - avgy) / (pooled_var * math.sqrt((1 / nx) + (1 + ny)))
cdf_z = t.cdf(stat_z, nx + ny - 2)
val_p = 2 * (1 - cdf_z)
print('CDF: ', cdf_z)
print('p-value: ', val_p)
