# Zamiana ułamka dziesiętnego do jego postaci w zapisie binarnym.
# Ewentualną część całkowitą nalęzy przekonwertować i dodać oddzielnie. 
n = 0.141
print('0.', end='')
while n > 0:
    n = n * 2
    if n >= 1:
        n = n - 1
        print(1, end='')
    else:
        print(0, end='')
print()

# Zamiana ułamka w zapisie binarnym do jego postaci dziesiętnej.
# Należy podać liczby po przecinku ułamka.
# Tutaj: 0.10110000101000111101 (0.69)
n = [int(x) for x in '10110000101000111101']
len_n = 6
i = 1
w = 0
while i <= len_n:
    if n[i - 1] != 0:
        w = w + 2 ** (-1 * i)
    i = i + 1    
print(w)