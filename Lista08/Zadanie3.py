from collections import Counter
from itertools import combinations

def load_word_dict(file):
    """Wczytanie listy słów z pliku tekstowego."""
    with open(file, 'r', encoding='utf-8') as f:
        return [word.strip().lower() for word in f.readlines()]

def riddle(input_name):
    """Generowanie par słów-krzyżówek."""
    char_name = input_name.lower().replace(' ', '') # Usunięcie spacji i zamiana na małe litery.
    char_count = Counter(char_name) # Liczba wystąpień liter w imieniu i nazwisku.
    
    valid_words = [word for word in word_dict if Counter(word) <= char_count] # Pasujące słowa.

    pairs = set()
    for word1, word2 in combinations(valid_words, 2): # Łączymy wszystkie dobre słowa w pary
        if Counter(word1 + word2) == char_count: # Sprawdzamy czy znaki w obu wyrazach są równe tym w wyrazie początkowym.
            if word1 not in char_name and word2 not in char_name: # Wejściowe dane nie mogą być w wyniku.
                pairs.add(tuple(sorted((word1, word2)))) # Zapisujemy wyrazy jako posortowane krotki, żeby się nie powtarzały.
    return sorted(pairs)

# Załadowanie słownika
word_file = 'popularne_slowa2023.txt'
word_dict = load_word_dict(word_file)

# Generowanie par krzyżówek
name_original = 'Antek Boryna'
name_pairs = riddle(name_original)

# Wypisywanie wyników
counter = 1
for name_pair in name_pairs:
    print(*name_pair, end=',\t')
    if not counter % 5: print()
    counter += 1