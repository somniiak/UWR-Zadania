import turtle as t
import random
from copy import deepcopy
from random import randint

def turtle_travel(kx, ky):
    """Względne przemieszczenie, bez rysowania."""
    t.penup()
    x, y = t.pos()
    x, y = x + kx, y + ky
    t.goto(x, y)
    t.pendown()


def draw_square(k):
    """Malowanie kwadratu."""
    t.colormode(255)
    t.begin_fill()
    for _ in range(4):
        t.forward(k)
        t.right(90)
    t.end_fill()
    t.forward(k)


def right_rot(dir):
    if dir == (1, 0):
        return (0, 1)

    elif dir == (0, 1):
        return (-1, 0)

    elif dir == (-1, 0):
        return (0, -1)

    elif dir == (0, -1):
        return (1, 0)

def left_rot(dir):
    if dir == (1, 0):
        return (0, -1)

    elif dir == (0, -1):
        return (-1, 0)

    elif dir == (-1, 0):
        return (0, 1)

    elif dir == (0, 1):
        return (1, 0)

class Player:

    def __init__(self, y_idx, x_idx):
        self.direction = (1, 0)
        self.position = (y_idx, x_idx)

    def move(self):
        ny = (self.position[0] + self.direction[0]) % board.MY
        nx = (self.position[1] + self.direction[1]) % board.MX
        self.position = (ny, nx)
        if board.board[ny][nx] == '#':
            board.board[ny][nx] = '.'
            self.direction = right_rot(self.direction)
        else:
            board.board[ny][nx] = '#'
            self.direction = left_rot(self.direction)


class Grid:

    def __init__(self, x=None, y=None, filename=None):
        """Obiekt planszy."""
        with open(filename, 'r', encoding='utf-8') as f:
                self.board = [list(line.strip()) for line in f.readlines()]
                self.MY = len(self.board)
                self.MX = len(self.board[0])

    def draw_grid(self):
        """Malowanie planszy."""
        # Ustawienie opcji
        t.speed(0)
        t.tracer(0)
        t.hideturtle()
        t.clear()

        # Zresetowanie pozycji
        offset_x = (-self.MX * K) // 2
        offset_y = (self.MY * K) // 2

        t.penup()
        t.goto(offset_x, offset_y)
        t.pendown()

        # Malowanie siatki
        for y in self.board:
            for x in y:
                if x == '#':
                    t.fillcolor('black')
                #elif x == '*':
                #    t.fillcolor('red')
                else:
                    t.fillcolor('white')
                draw_square(K)
            turtle_travel(-self.MX * K, -K)

        t.update()


# Rozmiar boku kwadratu
K = 40

# Plik z planszą
FILE = 'plansza.txt'

board = Grid(filename=FILE)
start_x = randint(0, 22)
start_y = randint(0, 14)
mrowka = Player(start_y, start_x)

while True:
    mrowka.move()
    board.draw_grid()
