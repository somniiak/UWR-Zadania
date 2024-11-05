from duze_cyfry import daj_cyfre
from random import choice
import turtle as t

def wypisz(n):
    n = [daj_cyfre(int(i)) for i in str(n)]
    arr = [''] * 5
    for i in range(5):
        for j in n:
            arr[i] += (j[i] + ' ')
    return arr

def drawS():
    for i in range(4):
        t.forward(k)
        t.right(90)
    t.forward(k)

# Liczba do namalowania
n = 69420
lines = wypisz(n)
# Dlugosc boku
k = 30
# Dostępne kolory
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink',
        'brown', 'firebrick', 'maroon', 'magenta', 'navy', 'peru', 'orchid']


# Dlugosc linijki
l = len(lines[0]) * k
# Losuj kolory
colors = [choice(colors) for i in range(len(str(n)))]
# Rozpocznij w widocznym miejscu
t.penup()
t.goto(-500, 100)

t.speed('fastest')
for line in lines:
    i = 0
    t.penup()
    for char in line:
        t.end_fill()
        if char == '#':
            t.pendown()
            t.fillcolor(colors[i // 6])
            t.begin_fill()
        else:
            t.penup()
        drawS()
        i += 1
    t.goto(t.pos() - (l, k))
t.Screen().exitonclick()