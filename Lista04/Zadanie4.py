def primeRange(n):
    nums = [0, 0] + [i for i in range(2, n + 1)]
    for i in range(2, n + 1):
        if nums[i]:
            k = i + i
            while k <= n:
                nums[k] = 0
                k += i
    return nums

palindromy = lambda a, b: [i for i in primeRange(b) if i >= a and str(i) == str(i)[::-1]]

x = primeRange(10 ** 6)
print(x)
#print(palindromy(500, 1000))
