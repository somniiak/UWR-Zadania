import random
import turtle as t
from copy import deepcopy


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


class Player:

    colors = {
        ('k', 1): (255, 127, 211), ('k', 2): (255, 100, 202), ('k', 3): (255, 71, 193), ('k', 4): (255, 44, 162), ('k', 5): (255, 29, 113),
        ('p', 1): (157, 255, 233), ('p', 2): (127, 255, 226), ('p', 3): (86, 255, 217), ('p', 4): (49, 255, 193), ('p', 5): (0, 255, 137),
        ('n', 1): (139, 229, 255), ('n', 2): (99, 220, 255), ('n', 3): (62, 197, 255), ('n', 4): (0, 156, 255), ('n', 5): (0, 115, 255),
    }

    def __init__(self, value, power, y_idx, x_idx):
        """Obiekt gracza (kamień, papier, nożyce)."""
        self.value = value
        self.power = power
        self.position = (y_idx, x_idx)
        self.color = Player.colors[(self.value, self.power)]


class Grid:

    def __init__(self, x=None, y=None, filename=None):
        """Obiekt planszy."""
        if not filename and x and y:
            self.MY = y
            self.MX = x
            self.board = [['.' for _ in range(self.MX)] for _ in range(self.MY)]

        elif filename and not x and not y:
            with open(filename, 'r', encoding='utf-8') as f:
                self.board = [list(line.strip()) for line in f.readlines()]
                self.MY = len(self.board)
                self.MX = len(self.board[0])

                # Losujemy dla wartości jakieś losowe siły
                # bo w przykładzie na liście nie było i
                # zapisujemy elementy jako obiekty.
                for y in range(self.MY):
                    for x in range(self.MX):
                        if self.board[y][x] != '.':
                            self.board[y][x] = Player(self.board[y][x], random.randint(1, 5), y, x)

        else:
            raise Exception('Żle wczytano planszę.')


    def randomize(self, count=15):
        """Losowanie przykładowej rozgrywki."""
        # Wyczyszczenie poprzedniej siatki
        self.board = [['.' for _ in range(self.MX)] for _ in range(self.MY)]

        for _ in range(count):
            # Wybór położenia
            rand_y = random.randint(0, self.MY - 1)
            rand_x = random.randint(0, self.MX - 1)

            # Wybór rodzaju i siły
            value = random.choice(['k', 'p', 'n'])
            power = random.randint(1, 5)

            # Strorzenie obiektu gracza
            player = Player(value, power, rand_y, rand_x)

            self.board[rand_y][rand_x] = player

    def print_grid(self):
        """Wypisanie planszy (do debugowania)."""
        for y in self.board:
            for x in y:
                if x != '.':
                    print(x.value, end='')
                else:
                    print(x, end='')
            print()

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
                if x != '.':
                    t.fillcolor(x.color)
                else:
                    t.fillcolor('white')
                draw_square(K)
            turtle_travel(-self.MX * K, -K)

        t.update()


def play(old_grid, new_grid, y, x):
    if isinstance(old_grid.board[y][x], Player):
        # Kim jest obecny gracz
        current_value = old_grid.board[y][x].value
        current_power = old_grid.board[y][x].power

        # Kierunki wyboru sąsiada
        directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1),
            #(1, 1), (-1, 1), (1, -1), (-1, -1)
            ]

        # Filtrujemy kierunki niewychodzące za siatkę
        valid_neighbors = [
            (y + dy, x + dx)
            for dy, dx in directions
            if 0 <= y + dy < old_grid.MY and 0 <= x + dx < old_grid.MX
        ]

        if valid_neighbors:
            ny, nx = random.choice(valid_neighbors)
        else:
            return

        # Sąsiad też jest graczem
        if isinstance(old_grid.board[ny][nx], Player):
            enemy_value = old_grid.board[ny][nx].value
            enemy_power = old_grid.board[ny][nx].power

            # Sąsiadem jest pole naszego koloru, nic się nie dzieje.
            if enemy_value == current_value:
                return

            # Pojedynek!!
            else:
                def enemy_victory():
                    if old_grid.board[y][x].power == 1:
                        new_grid.board[y][x] = '.'
                    else:
                        new_grid.board[y][x] = Player(current_value, current_power - 1, ny, nx)

                    if old_grid.board[ny][nx].power < 5:
                        new_grid.board[ny][nx] = Player(current_value, enemy_power + 1, ny, nx)

                def enemy_defeat():
                    if old_grid.board[ny][nx].power == 1:
                        new_grid.board[ny][nx] = '.'
                    else:
                        new_grid.board[ny][nx] = Player(current_value, enemy_power - 1, ny, nx)

                    if old_grid.board[y][x].power < 5:
                        new_grid.board[y][x] = Player(current_value, current_power + 1, ny, nx)

                if enemy_value == 'k':
                    if current_value == 'p': enemy_defeat() # Papier bije kamień - przegrana wroga
                    elif current_value == 'n': enemy_victory() # Kamień bije nożyce - wygrana wroga

                elif enemy_value == 'p':
                    if current_value == 'k': enemy_victory() # Papier bije kamień - wygrana wroga
                    elif current_value == 'n': enemy_defeat() # Nożyce biją papier - przegrana wroga

                elif enemy_value == 'n':
                    if current_value == 'k': enemy_defeat() # Kamień bije nożyce - przegrana wroga
                    elif current_value == 'p': enemy_victory() # Nożyce biją papier - wygrana wroga

        # Zasiedlamy sąsiada z niższą siłą.
        else:
            if current_power > 1:
                new_grid.board[ny][nx] = Player(current_value, current_power - 1, ny, nx)

# Rozmiar boku kwadratu
K = 40

# Plik z planszą
FILE = 'plansza.txt'


old_board = Grid(filename=FILE)
new_board = deepcopy(old_board)
while True:
    for y in range(old_board.MY):
        for x in range(old_board.MX):
            play(old_board, new_board, y, x)

    new_board.draw_grid()

    old_board = deepcopy(new_board)
    new_board = deepcopy(old_board)
