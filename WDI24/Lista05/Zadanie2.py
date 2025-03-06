from wdi import *

n = 100

k = 1
fact_k = 1
while k * fact_k <= n:
    k += 1
    fact_k *= k

res = Array(k)
fact_i = fact_k
for i in range(k, 0, -1):
        res[k - i] = n // fact_i
        n %= fact_i
        fact_i //= i

if res[0]:
    printf("%d ", res[0])
for i in range(1, k):
    printf("%d ", res[i])
