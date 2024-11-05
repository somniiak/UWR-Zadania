from random import randrange
import turtle as t

def getColor():
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    return (r, g, b)

def drawS():
    t.fillcolor(getColor())
    t.begin_fill()
    for i in range(4):
        t.forward(k)
        t.right(90)
    t.end_fill()
    t.forward(k)

# Ilosc kwadracikow
n = 20
# Dlugosc boku
k = 30

# Przygotowanie
t.penup()
t.goto(-300, 300)

t.speed('fastest')
t.colormode(255) 
for i in range(n):
    t.pendown()
    for j in range(n):
        drawS()
    t.penup()
    t.goto(t.pos() - (n * k, k))
t.Screen().exitonclick()