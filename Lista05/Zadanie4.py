######################################
#  usun_duplikaty.py
######################################

# cel: usun_duplikaty([1,2,3,1,2,6,7,7,7,0]) -> [1,2,3,6,7,0] 

def usun_duplikaty1(L): # wolna wersja
    wynik = []
    for e in L:
        if e not in wynik:   # not (e in wynik)
            wynik.append(e)
           
    return wynik
    
def usun_duplikaty2(L): # wersja ze zbiorami
    wynik = []
    elementy = set()
    for e in L:
        if e not in elementy: 
            wynik.append(e)        
            elementy.add(e)
           
    return wynik


usun_duplikaty = usun_duplikaty2
    
print (usun_duplikaty([1,2,3,1,2,6,7,7,7,0]))

N = 7
nowy = usun_duplikaty( list(range(10 ** N)))
print (len(nowy))