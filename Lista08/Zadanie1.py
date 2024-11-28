import re
import random
from collections import Counter
from collections import defaultdict as dd

pol_ang = dd(lambda:[])

with open('brown.txt', 'r') as f:
    brownList = re.findall('\w+', f.read().lower())
    brownDict = Counter(brownList)

for x in open('pol_ang.txt'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue    
    pol, ang = L
    pol_ang[pol].append(ang)
pol_ang = Counter(pol_ang)

def tlumacz(polskie):
    wynik = []
    for s in polskie:
        if s in pol_ang:
            ws = []
            for w in pol_ang[s]:
                ws.append((brownDict[w], w))
            wynik.append(max(ws)[1])
        else:
            wynik.append('[?]')
    return ' '.join(wynik)
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()
for i in range(5):
    print (tlumacz(zdanie))            
            
