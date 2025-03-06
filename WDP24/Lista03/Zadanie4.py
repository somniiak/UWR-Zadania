import turtle
import math

def drawShape(k = 150, n = 12):
    m = 360 // (2*n)
    for i in range(360):
        sinus = math.sin(i * (math.pi / m))
        turtle.forward(k * 1.5 + sinus * 40)
        turtle.goto(0, 0)
        turtle.right(1)

turtle.speed('fastest')
drawShape()
input()