from turtle import *
from random import randint

def gradient(bok):
    gradient = []
    a = list(getColor())
    b = list(getColor())
    for i in range(bok):
        step = tuple(int(a[j] + (b[j] - a[j]) * (i / (bok - 1))) for j in range(3))
        gradient.append(step)
    return gradient

def getColor():
    colormode(255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

def chooseColor(a):
    colormode(255)
    colors = {'1': (255, 0, 255), '2': (213, 34, 83), '3': (0, 255, 255),
              '4': (255, 128, 0), '5': (128, 128, 128), '6': (10, 200, 100)}
    fillcolor(colors[a])

def kwadrat(bok):
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

n = 0
i = 0
colors = 0
def sq_sides(s):
    global n
    n = s

def murek(s,bok):
    global i
    global n
    global colors
    for a in s:
        if a == 'f':
            kwadrat(bok)
            fd(bok)
        elif a == 'b':
            kwadrat(bok)
            fd(bok)         
        elif a == 'l':
            bk(bok)
            lt(90)
        elif a == 'r':
            rt(90)
            fd(bok)
        elif not a.isalpha():
            chooseColor(a)
        elif a == 'c':
            if not colors:
                colors = gradient(sum(list(range(2, n + 1))))
            fillcolor(colors[i])
            i += 1