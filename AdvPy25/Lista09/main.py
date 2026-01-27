# Inspiracje
# https//redd.it/1gur6m/
# https://rosettacode.org/wiki/Conway's_Game_of_Life

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

# Wymiary planszy
n = 100

# a=[1, 0] - możliwe wartości komórki
# size=(n, n) - rozmiary macierzy wyników
# p=[0.2, 0.8] - prawdopodobieństwo: 20% żywych i 80% martwych komórek
# https://www.geeksforgeeks.org/python/numpy-random-choice-in-python/
grid = np.random.choice(a=[1, 0], size=(n, n), p=[0.2, 0.8])

def update(data):
    global grid
    newGrid = grid.copy()

    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    for i in range(n):
        for j in range(n):
            total = sum(
                grid[(i + di) % n, (j + dj) % n]
                for di, dj in neighbors)

            if grid[i, j]:
                if total < 2 or total > 3:
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1

    mat.set_data(newGrid)
    grid = newGrid
    return [mat]


fig, ax = plt.subplots()
ax.set_axis_off()
fig.tight_layout()
mat = ax.matshow(grid, cmap='plasma')
ani = animation.FuncAnimation(fig, update, interval=100, save_count=50)
plt.show()
