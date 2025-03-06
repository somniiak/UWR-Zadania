from math import sqrt


def potega(a,n):
    wynik = 1
    for i in range(n):
       wynik = wynik * a
    return wynik
   
def kwadrat(n):
    for i in range(n):
       for j in range(n): 
          print ("* ", end="") # Spacja po gwiazdce dla upiększenia
       print()
      
def kwadrat2(n):
    for i in range(n):
       print (n * "#")      

# Wycięcie kodu niepotrzebnego w
# rozwiązaniu zadania.
'''
for i in range(10):
    print (i, 2 ** i, potega(2,i), sqrt(i))  # drukujemy kolejne liczby wraz z kolejnymi potęgami dwójki oraz kolejnymi pierwiastkami                  
print ()
'''

# Kwadraty z gwiazdek do 4 (zamiast liczb
# parzystych), a z hasztagów do 9 (+ zmniejszenie
# o 5 wartości 'i' w argumencie.)
for i in range(10):
    print ("Przebieg:",i)
    print (20 * "-")
    if i <= 4:
        kwadrat(3 + 2 * i)
    else:
        kwadrat2(3 + (i - 5))
    print()
