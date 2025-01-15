import turtle as t


def interpolate_color(color1, color2, factor):
    return tuple(int(color1[i] + (color2[i] - color1[i]) * factor) for i in range(3))


def get_color_gradient(colors, steps):
    gradient = []
    num_colors = len(colors)
    for i in range(num_colors):
        start_color = colors[i]
        end_color = colors[(i + 1) % num_colors]
        for step in range(steps):
            gradient.append(interpolate_color(start_color, end_color, step / steps))
    return gradient


base_colors = [
    (255, 0, 0), (255, 165, 0), (255, 255, 0), # Czerwony, pomarańczowy, żółty,
    (0, 128, 0), (0, 0, 255), (128, 0, 128)    # zielony, niebieski, fioletowy.
    ]

colors = get_color_gradient(base_colors, 50)


def turtle_travel(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def spiral(angle=0, size=300):
    t.clear()
    t.setheading(angle)
    turtle_travel(0, 0)
    for x in range(size):
        t.pencolor(colors[x % len(colors)])
        t.width(x / 100 + 1)
        t.forward(x)
        t.left(59)
    t.update()


t.colormode(255)
t.bgcolor('black')
t.speed('fastest')
t.tracer(0)

i = 0
while True:
    if i <= 650:
        spiral(i, i)
    else:
        spiral(i, 650)
        colors = colors[1:] + colors[:1]
    i += 5
input()