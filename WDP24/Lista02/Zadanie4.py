from duze_cyfry import daj_cyfre

def wypisz(n):
    n = [daj_cyfre(int(i)) for i in str(n)]
    for i in range(5):
        for j in n:
            print(j[i] + ' ', end='')
        print()

wypisz(12345)
