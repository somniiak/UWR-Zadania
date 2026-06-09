from statsmodels.stats.proportion import proportion_confint

data = []
with open('l14z05.csv') as f:
    data = [[int(y) for y in x.split(',')[1:]] for x in f.readlines()]

# gęgawa zywczjna - sukces
# gęgawa różowodzioba - porażka
# łączymy wszystkie lata bo mowa o populacji, nie o pojedynczym roku

alpha = 0.05

successes = sum([row[0] for row in data])
failures = sum([row[1] for row in data])

n = successes + failures

low, high = proportion_confint(
    count=successes,
    nobs=n,
    alpha=alpha,
    method='normal'
)

print(f'Udział = {successes/n:.4f}')
print('Udział procentowy w przedziale:')
print(f'({100*low:.2f}%, {100*high:.2f}%)')
