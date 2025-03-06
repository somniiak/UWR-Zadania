from wdi import *

def fTiter(n, m):
    # Tworzymy tablicę pomocniczą, która przechowa wyniki dla T(0, 0) do T(n, m)
    dp = Array(m + 1)
    # Inicjalizujemy warunki bazowe dla m = 0, czyli dp[m] = n dla każdego n
    for i in range(m + 1):
        dp[i] = i
    
    # Wykonujemy iteracje dla każdego n od 1 do n (budowanie wierszy)
    for i in range(1, n + 1):
        # Warunek bazowy T(n, 0) = n
        dp[0] = i
        # Obliczamy kolejne wartości dla j od 1 do m
        for j in range(1, m + 1):
            dp[j] = dp[j] + 2 * dp[j - 1]
    
    # Wynik końcowy jest w dp[m], po zakończeniu pętli dla n, m
    return dp[m]

x = fTiter(3, 4)
print(x)