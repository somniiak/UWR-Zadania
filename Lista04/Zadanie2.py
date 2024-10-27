# https://projecteuler.net/problem=2

x = [0, 1]
while True:
    num = x[0] + x[1]
    x[0], x[1] = x[1], num
    if num > 4000000:
        break
    elif num % 2 == 0:
        x.append(num)

print(x[2:], sum(x[2:]))