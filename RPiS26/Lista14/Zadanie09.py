from prettytable import PrettyTable
from scipy.stats import chisquare

observed = [42, 40, 18]
total = sum(observed)

ratio = [4, 4, 2]
ratio_sum = sum(ratio)

expected = [
    total * r / ratio_sum
    for r in ratio
]

chi2_stat, p_value = chisquare(
    f_obs=observed,
    f_exp=expected
)

table = PrettyTable(float_format='.2')
table.field_names = ['', 'A. anser', 'A. fabialis', 'A. brachyrhynchus']
table.add_row(['Obserwowane', *observed])
table.add_row(['Oczekiwane', *expected])

print(table, '\n')
print(f'chi2: {chi2_stat:.3f}')
print(f'p-val: {p_value:.3f}\n')

if p_value < 0.05:
    print('Odrzucamy H_0:')
    print('liczebności gatunków nie są w proporcji 4:4:2.')
else:
    print('Brak podstaw do odrzucenia H_0:')
    print('liczebności gatunków są w proporcji 4:4:2.')
