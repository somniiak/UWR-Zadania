def usun_w_nawiasach(s):
    if '(' in s:
        s = s[:s.index('(')] + s[s.index(')') + 1:]
        return usun_w_nawiasach(s)
    # Chwyty dla upiększenia tekstu.
    for i in ' ,.?!':
        s = s.replace(' ' + i, i)
    return s

s = "Ala ma kota (perskiego) z białym (puchatym) futrem, którego (często) głaszcze!"
print(s + '\n' + usun_w_nawiasach(s) + '\n')

s = 'Ulica (Krokodyli) była koncesją (naszego) miasta na rzecz (nowoczesności i) zepsucia (wielkomiejskiego).'
print(s + '\n' + usun_w_nawiasach(s) + '\n')

s = 'Cicho (wszędzie), głucho (wszędzie), co to będzie (co to będzie)?'
print(s + '\n' + usun_w_nawiasach(s) + '\n')