from itertools import permutations
from random import choice

# Load words from the file into a set for fast lookup
with open('popularne_slowa2023.txt', 'r') as f:
    wordSet = set(map(str.strip, f))

# Create a dictionary to map sorted characters to original words
wordDict = {}
for word in wordSet:
    sortedWord = ''.join(sorted(word))
    wordDict.setdefault(sortedWord, []).append(word)

def riddle(inputName):
    inputName = inputName.lower()
    # Generate unique permutations of the input name
    namePerms = set(permutations(inputName.replace(' ', '')))  # Remove spaces for permutations
    res = set()

    for perm in namePerms:
        # Split into two parts; since we removed spaces, we can only split at valid indices
        for i in range(1, len(perm)):  # Start from index 1 to avoid empty first part
            first = ''.join(sorted(perm[:i]))
            second = ''.join(sorted(perm[i:]))
            if first in wordDict and second in wordDict:
                firstChoice = choice(wordDict[first])
                secondChoice = choice(wordDict[second])
                combined1 = f'{firstChoice} {secondChoice}'
                combined2 = f'{secondChoice} {firstChoice}'
                
                # Add to results if not already present and not equal to inputName
                if combined1 != inputName and combined2 != inputName:
                    res.add(combined1)
                    res.add(combined2)

    return res

name = 'Bolesław Prus'
res = riddle(name)
print(res)
