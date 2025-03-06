from wdi import *

def func_a(n):
        if n % 2 == 0:
            return n
        else:
            return -n

def func_b(n):
    arr = Array(n)
    i = 1
    while i <= n:
        if i % 2 == 0:
            arr[i - 1] = 1 / i
        else:
            arr[i - 1] = -1 / i
        i = i + 1
    res = 0
    i = i - 2
    while i >= 0:
        res = res + arr[i]
        i = i - 1
    return res

def func_c(n, x):
    arr = Array(n)
    i = 1
    while i <= n:
        j = i
        y = x
        while j > 1:
            y = y * x
            j = j - 1
        arr[i - 1] = i * y
        i = i + 1
    res = 0
    i = i - 2
    while i >= 0:
        res = res + arr[i]
        i = i - 1
    return res

n = 5
x = 3

f1 = func_a(n)
printf("%d\n", f1)

f2 = func_b(n)
printf("%f\n", f2)

f3 = func_c(n, x)
printf("%f\n", f3)