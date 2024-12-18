def powerset(nums):
    res = []
    if not nums:
        return []
    else:
        for num in nums:
            tnums = nums[:]
            tnums.remove(num)
            res += tnums
            return res + powerset(tnums)

numbers = [1,2,3,100]
numbers = powerset(numbers)
print(numbers)