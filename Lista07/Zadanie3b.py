import re

with open('popularne_slowa2023.txt', 'r') as f:
    slowa = set(i.strip() for i in f.readlines())

with open('lalka-tom-pierwszy.txt', 'r') as f:
    lines = ' '.join([i.strip() for i in f.readlines()]).strip()
lines = [i.strip(':, ') for i in re.split('\w*[ĄąĆćĘęŁłŃńÓóŚśŻźŹż]\w*', lines) if re.sub('[\W ]+', '', i)]

res = []
for line in lines:
    words = re.findall('[\w]+', line)
    i = 0
    for word in words:
        if word in slowa:
            i += 1
    if i == len(words):
        res.append(line)

res = sorted([(len(re.sub(r'\W+', '', i)), i.strip(', ')) for i in res], reverse=True)

for i in range(5):
    print(f'...{res[i][1]}...')