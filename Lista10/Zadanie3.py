letters_chr = {char: idx for idx, char in enumerate('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')}
letters_num = {idx: char for idx, char in enumerate('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')}

def encode_num(word):
    return [letters_chr[letter] for letter in word]

def encode_chr(word):
    return [letters_num[number] for number in word]

def riddle(word):
    # Podział na części
    word = word.split()
    word.remove('+')
    word.remove('=')

    left = list(word[0])
    right = list(word[1])
    result = list(word[2])
    return result

word = riddle('send + more = money')
print(word)