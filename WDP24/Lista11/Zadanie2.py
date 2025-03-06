def PNF(word):
    letters = ''
    for letter in word:
        if letter not in letters:
            letters += letter
    letters = {l: v + 1 for v, l in enumerate(letters)}
    return '-'.join([str(letters[l]) for l in word])

print(PNF('indianin'))