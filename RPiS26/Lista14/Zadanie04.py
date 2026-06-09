from scipy import stats
from numpy import var

data = []
with open('l14z04.csv') as f:
    data = [float(y) for x in f.readlines() for y in x.split(',')]

females = data[::2]
males = data[1::2]

print("Wariancja samic:", var(females, ddof=1))
print("Wariancja samców:", var(males, ddof=1))
print()

_, p_norm1 = stats.shapiro(females)
_, p_norm2 = stats.shapiro(males)

# Test normalności
print("Shapiro samice p =", p_norm1)
print("Shapiro samce p =", p_norm2)
print()

# Test Welcha (nierówne wariancje)
stat, p_val = stats.ttest_ind(females, males, equal_var=False)

print("Statystyka t:", stat)
print("p =", p_val)
print()

if p_val < 0.05:
    print("Odrzucamy H0 - masa posiewnic wskazuje na dymorfizm.")
else:
    print("Brak podstaw do odrzucenia H0.")