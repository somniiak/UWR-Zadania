from kwadrat import kwadrat
from turtle import update, clear
import random
import sys


txt = """
.............###......
......................
............###.......
............###.......
......................
....###...........###.
......#...............
.....#................
...........###........
......................
..###.................
....#.................
...#............##....
................##....
"""

tab = [list(x) for x in txt.split()] 

MY = len(tab)
MX = len(tab[0])

def rysuj_plansze(tab):
    clear()
    for x in range(MX):
        for y in range(MY):
            if tab[y][x] == '#':
                kolor = 'green'
            else:
                kolor = 'lightgreen'
            kwadrat(x, MY-y, kolor)
    update()        

historia = set()

rysuj_plansze(tab)

KIERUNKI = [ (1,0), (0,1), (-1, 0), (0, -1), (1,1), (-1,1), (1,-1), (-1,-1)]

def liczba_sasiadow(x, y):
    ls = 0  
    for dx, dy in KIERUNKI:
        nx = (x + dx) % MX
        ny = (y + dy) % MY
        if tab[ny][nx] == '#':
            ls += 1
    return ls
   
def pusta_plansza():
    return [['.'] * MX for y in range(MY)]
            
# reguły gry w życie:
# jeżeli komórka pełna ma 2 lub 3 sąsiadów przeżywa, wpp ginie
# jeżeli komórka pusta ma 3 sąsiadów, to rodzi się nowa
#
#
def reprezentacja(t):
    return str(t)
    return tuple(tuple(wiersz) for wiersz in t)
    
while True:
    nowy_tab = pusta_plansza()
    for x in range(MX):
        for y in range(MY):
            ls = liczba_sasiadow(x, y)
            if ls == 3:
                nowy_tab[y][x] = '#'
            elif ls == 2 and tab[y][x] == '#':
                nowy_tab[y][x] = '#'
    
    rysuj_plansze(nowy_tab)
    
    r = reprezentacja(nowy_tab)
    if r in historia:
        break
    historia.add(r)
    tab = nowy_tab
    
     
    
    
print ('Koniec')
input()