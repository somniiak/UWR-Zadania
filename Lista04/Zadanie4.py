def primeRange(n):
    if n < 2:
        return []
    nums = list(range(2, n + 1))
    i = 0
    while i < len(nums):
        if nums[i] != 0:
            k = nums[i]
        else:
            i += 1
        for num in nums[i + 1:]:
            if num != 0 and num > k and num % k == 0:
                nums[nums.index(num)] = 0
        i += 1
    return nums

palindromy = lambda a, b: [i for i in primeRange(b) if i >= a and str(i) == str(i)[::-1]]

print(palindromy(500, 1000))