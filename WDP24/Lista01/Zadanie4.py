from losowanie_fragmentow import losuj_fragment
from random import choice
from random import shuffle

# Demonstracja działania funkcji
# w treści zadania.
# for i in range(5):
#     print (losuj_fragment())

def losuj_haslo(n):
    rozklad = []
    # Rozkład liczby jako sumy 2, 3 i 4
    # Realizacja pomysłu ChatemGPT
    for a in range(n // 2 + 1):
        for b in range(n // 3 + 1):
            for c in range( n // 4 + 1):
                if 2 * a + 3 * b + 4 * c == n:
                    # 2: a, 3: b, 4: c
                    rozklad.append((a, b, c))

    # Wybieramy tylko jedną z możliwości
    # rozkładu, żeby nie kombinować
    rozklad = choice(rozklad)
    haslo = []
    pwd2, pwd3, pwd4 = rozklad[0], rozklad[1], rozklad[2]
    for i in range(pwd2):
        frag = ''
        while len(frag) != 2:
            frag = losuj_fragment()
        haslo.append(frag)
    for i in range(pwd3):
        frag = ''
        while len(frag) != 3:
            frag = losuj_fragment()
        haslo.append(frag)
    for i in range(pwd4):
        frag = ''
        while len(frag) != 4:
            frag = losuj_fragment()
        haslo.append(frag)
    shuffle(haslo)
    return ''.join(haslo)


for i in range(10):
    print(losuj_haslo(8))
for i in range(10):
    print(losuj_haslo(12))
