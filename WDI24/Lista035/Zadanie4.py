a = [0, 1, 0, 1, 0, 1, 0, 0] # 42 odwrotnie
b = [0, 0, 1, 0, 0, 1, 0, 0] # 36 odwrotnie
k = 8

#a 00101010

c = [0, 0, 0, 0, 0, 0, 0, 0]
t = 0
i = 0
while i < k:
    c[i] = a[i] + b[i] + t
    if c[i] == 3:
        c[i] = 1
        t = 1
    elif c[i] == 2:
        c[i] = 0
        t = 1
    elif c[i] == 1:
        t = 0
    elif c[i] == 0:
        t = 0
    i = i + 1

i = k - 1
while i >= 0:
    print(c[i], end='')
    i = i - 1
    