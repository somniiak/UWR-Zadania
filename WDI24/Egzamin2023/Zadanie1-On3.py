X = [5, 7, 2, 4]
n = 4
k = 2

sval = 0
for i in range(n):
    sval = sval + X[i]
sval = sval // k

def sequence(sval):
    match = (0, 0)
    match_val = 0
    for i in range(n):
        val = X[i]
        if val >= match_val and val <= sval:
            match = (i, i)
            match_val = val
        for j in range(i + 1, n):
            val = val + X[j]
            if val >= match_val and val <= sval:
                match = (i, j)
                match_val = val
    return match

print(sequence(sval))