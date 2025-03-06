a = 25
b = 15

# Najmniejsza wspólna wielokrotność
def nww(a, b)
    return (a * b) / nwd(a, b)

# Algorymt Euklidesa
# Największy wspólny dzielnik
def nwd(a, b):
    if b != 0:
        return nwd(b, a % b)
    else:
        return a

print('NWD:', nwd(a, b))
print('NWW:', nww(a, b))