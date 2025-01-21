from itertools import product

with open('popularne_slowa2023.txt', 'r') as f:
    words = {i.strip() for i in f.readlines() if len(i.strip()) == 4}

alfabet = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'

def convert(start_word, end_word, path=[]):
    """Łamigłówka leksykalna."""

    def is_similar(first_word, second_word):
        """Czy słowa różnią się jedną literą."""

        if len(first_word) != len(second_word):
            return False

        differences = 0

        for letter1, letter2 in zip(first_word, second_word):
            if letter1 != letter2:
                differences += 1

        return differences == 1


    if len(start_word) != 4:
        return []

    if start_word == end_word:
        return path

    valid_words_start = [
        word for word in words
        if is_similar(start_word, word)
    ]

print(convert('mąka', 'keks'))
