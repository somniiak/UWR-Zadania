# Zamiana liczby binarnej do jej postaci dziesiętnej.
# Prymitywny pseudokodowy sposób.

b = 1111011
len_b = 7 - 1 # Ostania cyfra to 2^0
temp_b = 0
w = 0

# Odwracamy liczby kolejnością dla łatwości wykonania.
while b > 0:
    temp_b = temp_b * 10
    temp_b = temp_b + (b % 10)
    b = b // 10
while temp_b > 0:
    b = 1
    c = len_b
    while c > 0:
        b = b * 2
        c = c - 1
    w = w + b * (temp_b % 10)
    len_b = len_b - 1
    temp_b = temp_b // 10
print(w)