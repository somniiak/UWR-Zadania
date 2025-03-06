# Algorytm odwracający kolejność cyfr liczby

a = 12345
print(a)

b = 0
while a > 0:
    b = b * 10
    b += a % 10
    a = a // 10
print(b)