from scipy.stats import chi2
from statistics import variance

data = []

with open('z1206.csv', 'r') as f:
    data = [float(x) for x in f.readlines()]

n = len(data)
sigma_sqr = 16
mu = 2.8

# Podpunkt a)
S2 = variance(data)
stat_a = (n - 1) * S2 / sigma_sqr
F_a = chi2.cdf(stat_a, df=n-1)
print(f"a) chi2 = {stat_a:.5f}, F(chi2) = {F_a:.25f}")

# Podpunkt b)
stat_b = sum((x - mu)**2 for x in data) / sigma_sqr
F_b = chi2.cdf(stat_b, df=n)
print(f"b) chi2 = {stat_b:.5f}, F(chi2) = {F_b:.25f}")
