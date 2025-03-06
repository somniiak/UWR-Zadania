def pot(a, b):
    rez = 1
    while b > 0:
        if b % 2:
            rez = rez * a
        b = b // 2
        a = a * a
    return rez

n = 4
m = 390625

k = 1
while pot(n, pot(2, k)) < m:
    k += 1
print(k)
# Teraz mamy k takie, że n^(2*k) >= m.
# Musimy znaleźć najmniejsze k takie, że n^k >= m.

# Funkcja wykładnicza rośnie raptownie szybko.
# Nasze rozwiązanie znajduje się w najbliższej okolicy k.
bgn = pow(2, k - 1)
end = pow(2, k)
while bgn < end:
    mid = (bgn + end) // 2
    if pot(n, mid) < m:
        bgn = mid + 1
    else:
        end = mid
print(bgn)