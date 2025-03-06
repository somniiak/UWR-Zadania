import turtle


# Dlugosc boku
k = 100

# Ilosc poziomow
l = 7

# Tymczasowa pozycja
globalpos = ((-1 * k * l) / 2, (-1 * k * l) / 2)

turtle.left(90 - 30)
turtle.width(2)
turtle.speed('fastest')

def drawT(i):
    global globalpos
    for i in range(i):
       turtle.forward(k)
       if i == 0:
           globalpos = turtle.pos()
       turtle.right(120)
       turtle.forward(k)
       turtle.left(120)

for i in range(l, 0, -1):
    turtle.penup()
    turtle.goto(globalpos)
    turtle.pendown()
    drawT(i)

input()
