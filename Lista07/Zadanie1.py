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

i = 0
for line in lines:
    j = 0
    for color in line:
        x = offset_x + k * i
        y = offset_y - k * j
        podroz(x, y)
        kwadracik(k, color)
        j += 1
    i += 1
t.Screen().exitonclick()