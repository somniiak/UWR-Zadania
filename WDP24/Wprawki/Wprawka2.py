import turtle as t

def podroz(a, b):
    t.penup()
    t.goto((a, b))
    t.pendown()

def kwadrat(k):
    for i in range(4):
        t.forward(k)
        t.right(90)
    t.forward(k)

def rysuj(x = 0, y = 0, bok = 150, glebokosc = 0):
    if glebokosc == 0:
        t.begin_fill()
        kwadrat(bok)
        t.end_fill()
    else:
        for i in range(3):
            podroz(x, y - (bok / 3) * i)
            for j in range(3):
                if (j % 2 and not i % 2) or (not j % 2 and i % 2) :
                    podroz(t.pos()[0] + (bok / 3), t.pos()[1])
                else:
                    podroz(t.pos()[0], y - (bok / 3) * i)
                    rysuj(t.pos()[0], t.pos()[1], bok / 3, glebokosc - 1)

t.Screen().tracer(8)
t.speed('fastest')
rysuj(-300, 300, 600, 3)
t.Screen().update()
t.Screen().exitonclick()
