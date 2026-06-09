
from prettytable import PrettyTable
from scipy import stats

data = []
with open('l14z01.csv', 'r') as f:
    data = [[float(y) for y in x.split(',')] for x in f.readlines()]

towns = [[row[i] for row in data] for i in range(4)]

observed = [sum(t) for t in towns]
total = sum(observed)
expected = [total / 4] * 4

table = PrettyTable(float_format='.2')
table.field_names = ['', 'Msc. 1', 'Msc. 2', 'Msc. 3', 'Msc. 4']
table.add_row(['Obserwowane', *observed])
table.add_row(['Oczekiwane', *expected])
print(table, '\n')

stat, p_value = stats.chisquare(observed, expected)

print(f'chi2: {stat:.3f}')
print(f'p-val: {p_value:.3f}\n')

if p_value < 0.05:
    print('Odrzucamy H_0:')
    print('miejscowości nie są jednakowo akceptowalne.')
else:
    print('Brak podstaw do odrzucenia H_0:')
    print('miejscowości są w tym samym stopniu akceptowalne.')
