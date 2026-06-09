from prettytable import PrettyTable
from scipy import stats

# --------------------
# Test chi2
# https://home.agh.edu.pl/~bartus/index.php?action=dydaktyka&subaction=statystyka&item=test_chi2
# --------------------

rows = []
with open('l14z02.csv', 'r') as f:
    rows = [[int(y) for y in x.split(',')[1:]] for x in f.readlines()[1:]]
cols = [[rows[i][j] for i in range(len(rows))] for j in range(len(rows[0]))]

alpha = 0.05

# Miesiące
stat_month, p_month = stats.chisquare([sum(col) for col in cols])

# Siedliska
stat_hab, p_hab   = stats.chisquare([sum(row) for row in rows])

# Niezależność
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html
stat_dep, p_dep, df_dep, _ = stats.chi2_contingency(rows, correction=False)

# Wyniki
tests = [
    ('Miesiące', stat_month, len(cols) - 1, p_month),
    ('Siedliska', stat_hab, len(rows) - 1, p_hab),
    ('Miesiąc i siedlisko', stat_dep, df_dep, p_dep),
]

table = PrettyTable(float_format='.4')
table.field_names = ['', 'chi2-stat', 'df', 'p-val', 'Wniosek']
for name, stat, df, p in tests:
    table.add_row([
        name, stat, df, p,
        'Odrzucamy H_0' if p < alpha
        else 'Brak podstaw do odrzucenia H_0'
    ])

print(table)
