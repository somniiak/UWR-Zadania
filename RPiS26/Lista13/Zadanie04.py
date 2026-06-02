from scipy import stats

dataA, dataB, dataC = [], [], []

with open('rpr-1304.csv', 'r') as f:
    temp = [x.strip().split(',') for x in f.readlines()]
    dataA = [float(x) for x, y in temp if y == 'A']
    dataB = [float(x) for x, y in temp if y == 'B']
    dataC = [float(x) for x, y in temp if y == 'C']

# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html

stat, p_value = stats.f_oneway(dataA, dataB, dataC)
print(f"F = {stat:.5f}")
print(f"p-value = {p_value:.5f}")

# p = 0.00170 < 0.05 - odrzucamy hipotezę - istotne różnice między
# średnimi liczbami zgłoszeń w oddziałach A, B, C