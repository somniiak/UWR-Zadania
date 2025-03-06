n = 'AA10401AA' # Hex, 45651067306 Dec
m = len(n)

b = 0
for i in range(m // 2):
    if n[i] == n[m - i -1]:
        b = b + 1
if b == m // 2:
    print(True)
else:
    print(False)