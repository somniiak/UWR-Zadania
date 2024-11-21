import re
with open('lalka-tom-pierwszy.txt', 'r') as f:
    #                   (długość tekstu jako ciągu wyłącznie liter)       (podzielenie tekstu tam gdzie występuje słowo z polskimi znakami)
    lines = sorted([(len(re.sub(r'\W+', '', i)), i.strip(', ')) for i in re.split('\w*[ĄąĆćĘęŁłŃńÓóŚśŻźŹż]\w*', ' '.join([i.strip() for i in f.readlines()]))], reverse=True)
print(f'...{lines[0][1]}...')
