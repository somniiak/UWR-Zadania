from itertools import product

def to_num(word, perm):
    """Zamiana wyrazu na liczbę."""
    ans = 0

    for i in range(len(word)):
        ans *= 10
        ans += perm[word[i]]
    
    return ans

def riddle(word):
    """Znalezienie rozwiązania łamigłówki."""
    # Podział na części
    word = word.split()

    left = list(word[0])
    right = list(word[2])
    result = list(word[4])

    # Dopasowanie funkcji do operatora
    if word[1] == '+':
        f = lambda x, y: x + y
    elif word[1] == '-':
        f = lambda x, y: x - y
    elif word[1] == '*':
        f = lambda x, y: x * y
    else:
        f = lambda x, y: x / y

    letters = set(''.join(left + right + result))

    # Możliwe przypisania liczb (brute force)
    # Dopuszczamy powtórzenia liczb
    for prod in product(range(10), repeat=len(letters)):
        # Przypisanie liczb literom
        prod = dict(zip(letters, prod))

        lft = to_num(left, prod)
        rgt = to_num(right, prod)
        res = to_num(result, prod)

        if f(lft, rgt) == res:
            yield prod

for solution in riddle('kioto + osaka = tokio'):
    print(solution)