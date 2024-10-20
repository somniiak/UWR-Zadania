def isLucky(n):
    n = str(n)
    if len(n) < 3:
        return False
    elif '777' in n:
        return True
    else:
        return False    

def isPrime(n):
    while n > 1:
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                return False
        return True

liczby = [(i, isPrime(i)) for i in range(100001) if isLucky(i)]
print(liczby, len(liczby))