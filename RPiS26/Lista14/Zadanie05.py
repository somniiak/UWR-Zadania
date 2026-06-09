from prettytable import PrettyTable
from scipy.stats import chisquare

data = []
with open('l14z05.csv') as f:
    data = [[int(y) for y in x.split(',')[1:]] for x in f.readlines()]

alpha = 0.05
ratio = [2, 1]
ratio_sum = sum(ratio)

table = PrettyTable(float_format='.3')
table.field_names = ['Rok', 'Obs.', 'E', 'chi2', 'p', 'Czy 2:1?']

for year, observed in enumerate(data, 1):
    total = sum(observed)

    expected = [
        total * r / ratio_sum
        for r in ratio
    ]

    chi2_stat, p_value = chisquare(
        f_obs=observed,
        f_exp=expected
    )

    verdict = (
        "TAK" if p_value >= alpha else "NIE"
    )

    table.add_row([
        year,
        observed,
        [round(e, 3) for e in expected],
        chi2_stat,
        p_value,
        verdict
    ])

print(table)
