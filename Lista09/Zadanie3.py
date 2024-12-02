from collections import Counter, defaultdict
from itertools import combinations

def load_word_dict(file):
    """Wczytanie listy słów z pliku tekstowego."""
    with open(file, 'r', encoding='utf-8') as f:
        return [word.strip().lower() for word in f.readlines()]

def riddle(input_name):
    """Generowanie par słów-krzyżówek."""
    char_name = input_name.lower().replace(' ', '') # Usunięcie spacji i zamiana na małe litery.
    char_count = Counter(char_name) # Liczba wystąpień liter w imieniu i nazwisku.
    
    setSorted = lambda x: ''.join(sorted(x)) # Klucze słownika jako posortowane znaki, niestety Counter jest niehaszowalny.
    
    valid_words = defaultdict(lambda: [])
    valid_words.update({ # Słownik z komprehensji jest dodawany do defaultdict, aby zachować funkcję default.
        setSorted(word): word
        for word in word_dict
        if Counter(word) < char_count
    })

    trios = set()
    for word1, word2 in combinations(valid_words.values(), 2): # Łączymy wszystkie dobre słowa w pary (wartości w słowniku).
        word3 = valid_words[setSorted(char_count - Counter(word1 + word2))] # Wybieramy trzecie słowo z niewykorzystanych znaków.
        if word3 and Counter(word1 + word2 + word3) == char_count: # Sprawdzamy że trzecie słowo istnieje i wszystkie wyrazy spełniają specyfikację.
            if all(word not in input_name.lower().split() for word in (word1, word2, word3)): # Wejściowe dane nie mogą być w wyniku.
                trios.add(tuple(sorted((word1, word2, word3)))) # Zapisujemy wyrazy jako posortowane krotki, żeby się nie powtarzały.
    return trios

# Załadowanie słownika
word_file = 'popularne_slowa2023.txt'
word_dict = load_word_dict(word_file)

# Generowanie par krzyżówek
name_original = 'Bolesław Leśmian'
name_pairs = riddle(name_original)

# Wypisywanie wyników
counter = 1
for name_pair in name_pairs:
    print(*name_pair, end=',\t')
    if not counter % 5: print()
    counter += 1