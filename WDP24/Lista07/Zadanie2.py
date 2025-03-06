from random import choice
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

with open('niespodzianka.txt', 'r') as f:
    lines = [[eval(j) for j in i.strip().split()] for i in f.readlines()]

k = 15
t.tracer(1000)
t.speed('fastest')
t.colormode(255)

# Przesunięcie względem środka
offset_x = -len(lines) * k // 2
offset_y = len(lines[0]) * k // 2

index = [(i, j) for i in range(len(lines)) for j in range(len(lines[i]))]

for line in lines:
    for color in line:
        i, j = index.pop(index.index(choice(index)))
        color = lines[i][j]
        x = offset_x + k * i
        y = offset_y - k * j
        podroz(x, y)
        kwadracik(k, color)
t.Screen().exitonclick()