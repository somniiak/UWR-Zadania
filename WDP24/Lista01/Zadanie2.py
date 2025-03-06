def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)

lista = [i for i in range(4, 101)]

for liczba in lista:
    dlugosc = len(str(fact(liczba)))
    if dlugosc == 1:
        slowo = 'cyfrę'
    elif (dlugosc % 100 >= 12) and (dlugosc % 100 <= 14):
        slowo = 'cyfr'
    elif (dlugosc % 10 >= 2) and (dlugosc % 10 <= 4):
        slowo = 'cyfry'
    else:
        slowo = 'cyfr'
    print(f'{liczba}! ma', dlugosc, slowo)
