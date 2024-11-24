import re

with open('popularne_slowa2023.txt', 'r') as f:
    slowa = set(map(str.strip, f))

with open('lalka-tom-pierwszy.txt', 'r') as f:
    lines = re.split('\w*[ĄąĆćĘęŁłŃńÓóŚśŻźŹż]\w*', ' '.join(map(str.strip, f)))
lines = [re.sub('^\W+|[^a-zA-Z0-9!?-]+$', '', i) for i in lines if re.sub('[\W ]+', '', i)]

res = sorted({(len(re.sub('\W+', '', line)), line) for line in lines if all(word in slowa for word in re.findall('\w+', line))}, reverse=True)

for i in range(4):
    print(f'...{res[i][1]}...')