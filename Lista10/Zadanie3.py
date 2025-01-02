from itertools import permutations

def to_num(word, perm):
    """Zamiana wyrazu na liczbę."""
    ans = 0

    for i in range(len(word)):
        ans *= 10
        ans += perm[word[i]]
    
    return ans

def riddle(word):
    """Znalezienie rozwiązania krzyżówki."""
    # Podział na części
    word = word.split()
    word.remove('+')
    word.remove('=')

    left = list(word[0])
    right = list(word[1])
    result = list(word[2])

    letters = set(''.join(word))

    # Możliwe przypisania liczb jako permutacje
    for perm in permutations(range(10), len(letters)):
        # Przypisanie liczb literom
        perm = dict(zip(letters, perm))

        lft = to_num(left, perm)
        rgt = to_num(right, perm)
        res = to_num(result, perm)

        if lft + rgt == res:
            return perm

    return None

word = riddle('ciacho + ciacho = nadwaga')
print(word)