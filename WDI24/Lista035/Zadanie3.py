from wdi import *

n = 84
k = 8
num = Array(k)

for i in range(k):
    num[i] = 0

i = 0
ujemna = 0

min = -(2 ** (k - 1))
max = (2 ** (k - 1)) - 1
if n < min:
    printf("Poza zakresem.")
    exit()
elif n > max:
    printf("Poza zakresem.")
    exit()

if n < 0:
    ujemna =  1

m = n * n
m = m ** 0.5

while m > 0:
    num[i] = m % 2
    m = m // 2
    i = i + 1

i = 0
if ujemna == 1:
    while i < k:
        if num[i] == 0:
            num[i] = 1
        elif num[i] == 1:
            num[i] = 0
        i = i + 1
    i = 0
    t = 0
    num[0] = num[0] + 1
    while i < k:
        num[i] = num[i] + t
        if num[i] == 3:
            num[i] = 1
            t = 2
        elif num[i] == 2:
            num[i] = 0
            t = 1
        elif num[i] == 1:
            t = 0
        elif num[i] == 0:
            t = 0
        i = i + 1


for i in range(k):
    printf("%d", num[k-i-1])