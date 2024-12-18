letters_chr = {char: idx for idx, char in enumerate('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')}
letters_num = {idx: char for idx, char in enumerate('aąbcćdeęfghijklłmnńoóprsśtuwyzźż')}

def encode_num(word):
    return [letters_chr[letter] for letter in word]

def encode_chr(word):
    return [letters_num[number] for number in word]

def riddle(words):
    for word in words:
        print(encode_num(word))

riddle(['mleko', 'bazylia'])
