
def FibChange(n):
    coins = [1, 2]
    while coins[-1] + coins[-2] < n:
        coins.append(coins[-1] + coins[-2])

    change = []
    for coin in coins[::-1]:
        if n - coin >= 0:
            n -= coin
            change.append(coin)

    return (n == 0, change)

print(FibChange(2604))