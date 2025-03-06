n = 0.6
u = ''
r = []
rlen = 0

while n > 0:
    n = round(n * 2, 2)
    if n in r:
        print(rlen)
        break
    elif n >= 1:
        n = round(n - 1, 2)
        u = u + '1'
        rlen += 1
        r.append(n)
    else:
        u = u + '0'
        rlen += 1
        r.append(n)
if n == 0:
    rlen = 0
    print(rlen)