X = [5, 7, 2, 4]
n = 4
k = 2

def sequence():

    # Szukana wartość
    sval = 0
    for i in range(n):
        sval = sval + X[i]
    sval = sval // k

    # Obecna wartość
    cval = 0
    for i in range(k):
        cval = cval + X[i]

    match_i = 0
    match_j = k - 1

    diff_best = float('inf')

    for i in range(n - k + 1):
        diff_curr = cval - sval if cval >= sval else sval - cval

        if diff_curr <= diff_best:
            diff_best = diff_curr
            match_i = i
            match_j = i + k - 1

        if i + k < n:
            cval = cval - X[i] + X[i + k]

    return (match_i, match_j)

print(sequence())