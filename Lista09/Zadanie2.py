import turtle as t

def draw_square(k):
    """Malowanie kwadratu."""
    t.fillcolor('black')
    t.begin_fill()
    for _ in range(4):
        t.forward(k)
        t.right(90)
    t.end_fill()
    t.forward(k)

def turtle_travel(kx, ky):
    """Względne przemieszczenie, bez rysowania."""
    t.penup()
    x, y = t.pos()
    x, y = x + kx, y + ky
    t.goto(x, y)
    t.pendown()

def sierpinski(k, n):
    """Rekurencyjny dywan Sierpińskiego."""
    if n == 1:
        # Pierwszy rząd
        for _ in range(3):
            draw_square(k)
        turtle_travel(-3 * k, -k)

        # Drugi rząd
        draw_square(k)
        turtle_travel(k, 0)
        draw_square(k)
        turtle_travel(-3 * k, -k)

        # Trzeci rząd
        for _ in range(3):
            draw_square(k)
    
    else:
        # Pierwszy rząd (rekurencyjny)
        for _ in range(2):
            sierpinski(k / 3, n - 1)
            turtle_travel(0, 2 * k / 3)
        sierpinski(k / 3, n - 1)
        turtle_travel(-3 * k, -k / 3)

        # Drugi rząd (rekurencyjny)
        sierpinski(k / 3, n - 1)
        turtle_travel(k, 2 * k / 3)
        sierpinski(k / 3, n - 1)
        turtle_travel(-3 * k, -k / 3)

        # Trzeci rząd (rekurencyjny)
        for _ in range(3):
            sierpinski(k / 3, n - 1)
            turtle_travel(0, 2 * k / 3)
        t.update()

k = 200 # Długość boku kwadratu
n = 5 # Głębokość rekurencji

# Przyśpieszenie malowania
t.speed('fastest')
t.hideturtle()
t.tracer(0, 1)

# Przesunięcie siatki
offset_x = (-3 * k) // 2
offset_y = (3 * k) // 2
turtle_travel(offset_x, offset_y)

sierpinski(k, n)

t.Screen().exitonclick()