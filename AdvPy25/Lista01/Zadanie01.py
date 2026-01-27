from decimal import Decimal as dec

def vat_faktura(lista):
    lista = [dec(str(item)) for item in lista]
    return sum(lista) * dec('0.23')
    # return sum(lista) * 0.23

def vat_paragon(lista):
    lista = [dec(str(item)) for item in lista]
    return sum([item * dec('0.23') for item in lista])
    # return sum([item * 0.23 for item in lista])

zakupy = [0.1, 0.1, 0.1]

print(vat_faktura(zakupy) == vat_paragon(zakupy))
