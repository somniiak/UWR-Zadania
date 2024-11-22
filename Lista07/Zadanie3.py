import re

with open('popularne_slowa2023.txt', 'r') as f:
    slowa = set(i.strip() for i in f.readlines())

with open('lalka-tom-pierwszy.txt', 'r') as f:
    lines = re.sub('[ ]{2,}', ' ', ' '.join([i.strip() for i in f.readlines()]))
lines = [i.strip(',.?!-:;— ') for i in re.split('\w*[ĄąĆćĘęŁłŃńÓóŚśŻźŹż]\w*', lines) if re.sub('[\W ]+', '', i)]

res = []
for line in lines:
    count = 0
    words = re.findall('\w+', line)
    for word in words:
        if word in slowa:
            count += 1
    if count == len(words):
        while not line[0].isalpha():
            line = line[1:]
        res.append((len(re.sub(r'\W+', '', line)), line))
res = sorted(set(res), reverse=True)

for i in range(4):
    print(f'...{res[i][1]}...')