n = 798897
nums = [0] * 10

while n > 0:
    nums[n % 10] = 1
    n = n // 10
k = 0
for i in range(10):
    if nums[i]:
        k = k + 1
print(k)