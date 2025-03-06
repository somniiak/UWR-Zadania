from wdi import *

def nwd(a, b):
    if b != 0:
        return nwd(b, a % b)
    else:
        return a

n = 5
arr = Array(n)
arr = [45, 60, 15, 30, 15]
while n >= 0:
    for i in range(n - 1):
        arr[i] = nwd(arr[i], arr[i + 1])
        arr[i + 1] = 0
    n = n - 1
b = arr[0]
printf("%d\n", b)