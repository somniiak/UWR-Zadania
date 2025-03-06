n = 123412
m = 223411

num_n = [0] * 10
num_m = [0] * 10

while n > 0:
    num_n[n % 10] = num_n[n % 10] + 1
    n = n // 10
while m > 0:
    num_m[m % 10] = num_m[m % 10] + 1
    m = m // 10

c = 0
for i in range(10):
    if num_n[i] == num_m[i]:
        c = c + 1
if c == 10:
    print(True)
else:
    print(False)