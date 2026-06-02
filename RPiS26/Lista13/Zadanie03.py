from statistics import NormalDist
from math import sqrt

def isAlmost(current, target, eps=1e-6):
    return abs(current - target) <= eps

def binarySearchDistInv(targetVal, dist):
  left, right = -10.0, 10.0

  while right - left > 1e-6:
    mid = (left + right) / 2
    mid_val = dist(mid)

    if isAlmost(mid_val, targetVal):
            return mid

    if mid_val < targetVal:
            left = mid
    else:
            right = mid

  return (left + right) / 2

datax, datay = [], []

with open('rpr-1301.csv', 'r') as file:
    temp = [[float(y) for y in x.strip().split(',')] for x in file.readlines()]
    datax = [x[0] for x in temp]
    datay = [x[1] for x in temp]

nx = len(datax)
ny = len(datay)

avgx = sum(datax) / nx
avgy = sum(datay) / ny

dist = NormalDist(0, 1).cdf
# res = NormalDist(0, 1).inv_cdf(0.975)
res = binarySearchDistInv(0.975, dist)

CI_X = (avgx - res * 2/sqrt(nx), avgx + res * 2/sqrt(nx))
CI_Y = (avgy - res * 3/sqrt(ny), avgy + res * 3/sqrt(ny))

print(f"mu_X: ({CI_X[0]:.4f}, {CI_X[1]:.4f})")
print(f"mu_Y: ({CI_Y[0]:.4f}, {CI_Y[1]:.4f})")