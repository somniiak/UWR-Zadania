from random import randint
import turtle as t



def kwadracik(k, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.fd(k)
        t.right(90)
    t.end_fill()


def getColor(height, maxHeight, minHeight):
    """Przelicz indeks koloru na podstawie wartości wysokości."""
    mx = maxHeight - minHeight
    hg = height - minHeight
    if mx == 0:
        return 0  # Gdy wszystkie wartości w macierzy są takie same
    index = int(round((hg / mx) * (len(kolory) - 1), 0))
    return index


def meanWeighted(x, y):
    weights = [
        [2, 2, 2],  # Wagi dla sąsiadów
        [2, 3, 2],  # Punkt centralny (x, y) ma największą wagę
        [2, 2, 2],
    ]
    weighted_sum = 0
    weight_sum = 0
    
    for i in range(-1, 2):  # Sprawdzanie sąsiadów w zakresie od -1 do 1
        for j in range(-1, 2):
            nx, ny = x + i, y + j
            if 0 <= nx < rows and 0 <= ny < columns:  # Upewnienie się, że współrzędne są w granicach
                weighted_sum += grid[nx][ny] * weights[i + 1][j + 1]
                weight_sum += weights[i + 1][j + 1]
    
    return weighted_sum // weight_sum if weight_sum > 0 else 0


# Rozmiar boku kwadratu
k = 8
# Wymiary macierzy
rows, columns = 100, 100
# Macierz
grid = [[0 for _ in range(columns)] for _ in range(rows)]
# Kolory
kolory = ['green', (127, 255, 0), 'yellow', 'orange', 'red', (127, 0, 0)]

# Losowanie niezerowych wartości
for _ in range(1500):
    grid[randint(0, rows - 1)][randint(0, columns - 1)] = randint(1500, 2500)

# Losowanie średniej ważonej
for _ in range(int(33 * (rows * columns))):
    x = randint(0, rows - 1)
    y = randint(0, columns - 1)
    grid[x][y] = meanWeighted(x, y)

# Przygotowanie rysowania
t.tracer(0, 1)
t.speed('fastest')
t.penup()
t.colormode(255)

# Rysowanie siatki
offset_x = -columns * k // 2  # Przesunięcie względem środka
offset_y = rows * k // 2

# Wyznaczenie maksymalnej i minimalnej wartości w macierzy
maxHeight = max(max(row) for row in grid)
minHeight = min(min(row) for row in grid)

# Malowanie niepustych elementów siatki
for i in range(rows):
    for j in range(columns):
        x = offset_x + k * j
        y = offset_y - k * i
        t.goto(x, y)
        color_index = getColor(grid[i][j], maxHeight, minHeight)
        color = kolory[color_index]
        kwadracik(k, color)

t.done()
