def usun_duplikaty(n):
    n = sorted(list(enumerate(n)), key=lambda n: n[1])
    n = [n[0]] + [n[i] for i in range(1, len(n)) if n[i][1] != n[i - 1][1]]
    return [i[1] for i in sorted(n)]

L = [5,1,4,1,2,3,1,2,3,8,2,2,2,9,9,4]
L = usun_duplikaty(L)
print (L)