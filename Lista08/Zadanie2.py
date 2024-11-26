def ukladane(word, base):
    letterCount = lambda word: {i: word.count(i) for i in set(word)}
    word, base = letterCount(word), letterCount(base)
    for k, v in word.items():
        if not v <= base[k]:
            return False
    return True

x = ukladane('motyl', 'lokomotywa')
print(x)