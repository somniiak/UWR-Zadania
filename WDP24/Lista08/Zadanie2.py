from collections import Counter

ukladane = lambda x, y: Counter(x) <= Counter(y)
x = ukladane('motyl', 'lokomotywa')
print(x)