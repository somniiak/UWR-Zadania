from random import randint, choice
from duze_cyfry import daj_cyfre
import numpy as np
import turtle as t



def podroz(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def kwadracik(k, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.fd(k)
        t.right(90)
    t.end_fill()


def losuj_pozycje():
    x = randint(0, rows - 5)
    y = randint(0, columns - 5)
    return [x, y]


def czy_miejsce_wolne(pos, lines):
    x, y = pos
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                if grid[x + i][y + j]:
                    return False
    return True


def znajdz_sasiednie_kolory(pos, lines):
    x, y = pos
    kolory = set()
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for dx, dy in directions:
                    nx, ny = x + i + dx, y + j + dy
                    try:
                        if grid[nx][ny]:
                            kolory.add(int(grid[nx][ny]))
                    except IndexError:
                        pass
    return kolory


def wpisz_cyfre(n):
    global grid
    lines = daj_cyfre(n)

    # Sprawdzanie czy można wpisać liczbę w wylosowane
    # miejsce. Limit prób, aby zapobiec zapętleniu.
    for i in range(20):
        pos = losuj_pozycje()
        if czy_miejsce_wolne(pos, lines):
            break
    else:
        return
    
    # Sprawdzanie z jakimi kolorami sąsiaduje liczba i
    # wybranie koloru innego niż znalezione.
    zajete_kolory = znajdz_sasiednie_kolory(pos, lines)
    dostepne_kolory = list(set(range(len(colors))) - zajete_kolory)

    # W przypadku gdy jest mało kolorów do wyboru i nie można
    # wybrać innego koloru wychodzimy z funkcji.
    try:
        color_index = choice(dostepne_kolory)
    except IndexError:
        return

    # Malowanie liczby w siatce w postaci
    # indeksu jej koloru.
    x, y = pos
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '#':
                grid[x + i, y + j] = color_index



# Rozmiar boku kwadratu
k = 20
# Ilość liczb w siatce:
liczby = 100
# Wymiary sitaki
rows, columns = 40, 40
# Siatka stringów
grid = np.empty((rows, columns), dtype=str)
# Dostępne kolory
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'magenta', 'brown']

# Przygotowanie rysowania
t.tracer(0, 1)
t.speed('fastest')
t.width(2)

# Rysowanie siatki
offset_x = -columns * k // 2  # Przesunięcie względem środka
offset_y = rows * k // 2

# Losowanie liczb do namalowania
for i in range(liczby):
    wpisz_cyfre(randint(0, 9))
# Malowanie niepustych elementów siatki
for i in range(rows):
    for j in range(columns):
        # Jeśli komórka nie jest pusta - maluj
        if grid[i][j]:
            x = offset_x + k * j
            y = offset_y - k * i
            podroz(x, y)
            color_index = int(grid[i][j])
            color = colors[color_index]
            kwadracik(k, color)
t.done()