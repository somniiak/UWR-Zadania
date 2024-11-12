def podziel(s):
    i = 0
    arr = []
    for letter in s:
        if not letter.isspace():
            arr.append((i, letter))
        else:
            i += 1
    res = {}
    for k, v in arr:
        if k in res:
            res[k] += v
        else:
            res[k] = '' + v
    return list(res.values())

text = '  Ala   ma       kota , ktorego bardzo    kocha'
text = podziel(text)
print(text)