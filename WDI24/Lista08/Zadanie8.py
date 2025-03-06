from wdi import *

def printarr(arr):
    print('[', end='')
    for i in range(k):
        print(arr[i], end='')
        if i != k - 1:
            print(', ', end='')
    print(']', end='')

def hanoi(n, A, B, C):
    """słupki A, B, C są listami"""
    if n > 0:
        hanoi(n - 1, A, C, B)

        element = A[0] # Element z góry A przenieś na górę C
        for i in range(1, k): # Przesuń elementy w A w lewo
            A[i - 1] = A[i]
        A[k - 1] = 0  # Ostatnie miejsce w A ustaw na "puste", inaczej pozostałoby bez zmian

        # Przesuń elementy w C w prawo
        for i in range(k - 1, 0, -1):
            C[i] = C[i - 1]
        C[0] = element  # Umieść element na początku C
        
        printarr(A); printarr(B); printarr(C); print()
        hanoi(n-1, B, A, C)

k = 7
A = Array(k)
B = Array(k)
C = Array(k)

for i in range(k):
    A[i], B[i], C[i] = i + 1, 0, 0

printarr(A); printarr(B); printarr(C); print()
hanoi(k, A, B, C)