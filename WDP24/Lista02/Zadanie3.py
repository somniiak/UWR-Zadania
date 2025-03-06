# Funkcja malująca koło. Dodatkowy argument 'duzeKolo'
# przyjmuje wymiary dużego okręgu do którego należy
# wyrównać malowane koło (przy budowaniu bałwanka).
def kolko(n, *duzeKolo):
    srodek = n // 2
    promien = n / 2
    for y in range(n):
        if duzeKolo:
                print(' ' * ((duzeKolo[0] - n) // 2 ), end='')
        for x in range(n):
            # Równanie okręgu (x - a)^2 + (y - b)^2 = r^2
            odleglosc = ((x - srodek) ** 2 + (y - srodek) ** 2) ** 0.5
            if odleglosc <= promien:
                print('#', end='')
            else:
                print(' ', end='')
        print()

kolko(7, 15)
kolko(9, 15)
kolko(15)