from random import choice, sample

with open('slowa.txt', 'r') as f:
    wordSet = set(map(str.strip, f))

wordDict = {}
for word in wordSet:
    sortedWord = ''.join(sorted(word))
    wordDict.setdefault(sortedWord, []).append(word)

def riddle(inputName):
    # Generuj permutacje slowa
    shuffleWord = lambda word: ''.join(sample(word.lower(), len(word)))
    # Postoruj litery wyrazu
    setSorted = lambda word: ''.join(sorted(word))
    
    # Generowanie permutacji slow
    namePerms = []
    for _ in range(999999):
        tempWord = shuffleWord(inputName)
        if tempWord[0] != ' ' and tempWord[-1] != ' ':
            tempWord = tempWord.split()
            firstWord = setSorted(tempWord[0])
            secondWord = setSorted(tempWord[1])
            if firstWord in wordDict and secondWord in wordDict:
                firstWord = choice(wordDict[firstWord])
                secondWord = choice(wordDict[secondWord])
                tempWord = [firstWord, secondWord]
                # Permutacje nie moga sie powtarzac
                if not sorted(tempWord) in namePerms:
                    if not sorted(tempWord, reverse=True) in namePerms:
                        # Permutacja nie moze byc poczatkowym imieniem
                        if sorted(tempWord) != inputName.lower().split():
                            if sorted(tempWord, reverse=True) != inputName.lower().split():
                                namePerms.append(tempWord)
    namePerms = sorted([' '.join(perm) for perm in namePerms])
    return namePerms

name = 'Maciej Boryna'
res = riddle(name)
print(res)
