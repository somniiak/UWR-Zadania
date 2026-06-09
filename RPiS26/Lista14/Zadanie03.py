from scipy import stats
from numpy import var

data = []
with open('l14z03.csv') as f:
    data = [int(y) for x in f.readlines() for y in x.split(',')]

gegawa = data[::2]
posiewnica = data[1::2]

var_gegawa = var(gegawa, ddof=1)
var_posiewnica = var(posiewnica, ddof=1)

print("Wariancja gęgawy:", var_gegawa)
print("Wariancja posiewnicy:", var_posiewnica)
print()

_, p_norm1 = stats.shapiro(gegawa)
_, p_norm2 = stats.shapiro(posiewnica)

# Test normalności
print("Shapiro gęgawa p =", p_norm1)
print("Shapiro posiewnica p =", p_norm2)
print()

# Test Welcha (nierówne wariancje)
stat, p_val = stats.ttest_ind(gegawa, posiewnica, equal_var=False)

print("Statystyka t:", stat)
print("p =", p_val)
print()

if p_val < 0.05:
    print("Odrzucamy H0 - rozpiętość skrzydeł jest istotnie różna.")
else:
    print("Brak podstaw do odrzucenia H0.")