def isPrime(n):
    while n > 1:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        return True

def primeDiv(n):
    i = n
    res = set()
    while i > 1:
        if not n % i:
            if isPrime(i):
                n //= i
                res.add(i)
        i -= 1
    return res

n = 1234567
n = primeDiv(n)
print(n)