from turtle import *

i = 0

def get_i():
    return i

def inc_i():
    global i
    i += 1

def kwadracik(n):
    while n:
        fillcolor(colors[get_i()])
        begin_fill()
        for i in range(4):
            forward(k)
            right(90)
        end_fill()
        forward(k)
        inc_i()
        n -= 1

# Bok jednego kwadracika
k = 25
# Liczba pasków z kwadratów
n = 19

speed('fastest')
boki = list(range(2, n + 1))

colormode(255)
color1 = [230, 255, 26]
color2 = [230, 38, 156]
color_change = []
for i in range(3):
    color_change.append((color2[i] - color1[i]) / sum(boki))

colors = [(
            int(color1[0] + color_change[0] * i),
            int(color1[1] + color_change[1] * i),
            int(color1[2] + color_change[2] * i),
            )
            for i in range(sum(boki) + 2)]

for bok in boki:
    kwadracik(bok)
    right(90)
input()