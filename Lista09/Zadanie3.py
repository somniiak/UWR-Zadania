import re

def load_word_dict(file):
    """Wczytanie listy słów z pliku tekstowego."""
    with open(file, 'r', encoding='utf-8') as f:
        return [word.strip().lower() for word in f.readlines()]

def sy_la_by(slowo):
    return re.findall(r'[b-df-hj-np-tv-xz]*[aeiouy]*', slowo.lower())[:-1]

def wyszukaj_rym(slowo, liczba_sylab):
    return [word for word in word_dict if sy_la_by(word)[-liczba_sylab:] == sy_la_by(slowo)[-liczba_sylab:] and word != slowo]

# Wczytaj plik ze słowami
word_file = 'popularne_slowa2023.txt'
word_dict = load_word_dict(word_file)

# Wyszukiwanie rymów
word = wyszukaj_rym('przenica', 2)
print(word)