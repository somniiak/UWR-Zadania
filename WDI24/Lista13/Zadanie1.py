from random import randint
from wdi import *

def print2d(arr):
    print('[', end='')
    for i in range(len(arr)):
        print('[', end='')  # Wcięcie dla lepszej czytelności
        for j in range(len(arr[i])):
            print(arr[i][j], end='')
            if j < len(arr[i]) - 1:  # Unikamy przecinka na końcu wiersza
                print(', ', end='')
        print('],', end='')  # Zamknięcie wiersza z przecinkiem
    print(']')

n = 5

arr = Array(n)
for a in range(n):
    arr[a] = Array(n)

for i in range(n):
    for j in range(n):
        arr[i][j] = randint(0, 1)

print2d(arr)

# Macierz -> Lista
arr2list = Array(n)
for i in range(n):
    arr2list[i] = None
    for j in range(n):
        temp = arr2list[i]
        if arr[i][j]:
            arr2list[i] = ListItem(j)
            arr2list[i].next = temp

print()
for i in range(n):
    print(i, end=': ')
    arr2list[i].print_list()
print()

# Lista -> Macierz
marr = Array(n)
for i in range(n):
    marr[i] = Array(n)

for i in range(n):
    while arr2list[i]:
        marr[i][arr2list[i].value] = 1
        arr2list[i] = arr2list[i].next

print2d(marr)
