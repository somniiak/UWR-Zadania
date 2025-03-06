n = 7736377

a = n
b = 0
while a > 0:
    b = b * 10
    b += a % 10
    a = a // 10

if n == b:
    print(True)
else:
    print(False)