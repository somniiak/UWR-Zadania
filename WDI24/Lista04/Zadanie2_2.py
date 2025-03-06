def nwd(a, b):
    if b != 0:
        return nwd(b, a % b)
    else:
        return a

a = 15
b = 200
x = nwd(a, b)
print(f"{a}/{b} = {a//x}/{b//x}")