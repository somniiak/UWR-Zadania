from random import choice, randint
from re import finditer

with open('imiona_meskie.txt', 'r', encoding='utf8') as f:
    male_names = [f'{name.strip()}$' for name in f.readlines()]

with open('imiona_zenskie.txt', 'r', encoding='utf8') as f:
    female_names = [f'{name.strip()}$' for name in f.readlines()]

def get_char(current, names):
    """Generowanie litery do dodanie."""
    letters = {l: 0 for l in 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'}
    postfix = current[-2:] # Końcówka

    # Wyszukiwanie pozycji całej końcówki zamiast
    # pojedyńczych liter, bo jest problem gdy
    # litery się powtarzają.
    for name in names:
        for match in finditer(postfix, name):
            if name[match.end()] != '$':
                letters[name[match.end()]] += 1

    # Zbicie liter w jeden string powtarzając je
    # według ich wystąpień, aby wybierdać z
    # odpowiednim prawdopodobieństwem.
    mesh = ''.join([k * v for k,v in letters.items()])

    # Może się zdarzyć, że wyjdzie dziwna końcówka
    # do której nie pasują żadne litery.
    if not mesh:
        return None

    return choice(mesh)

def generate_name(gender='m', min_length=4, max_mength=10):
    """Generowanie imienia."""
    if gender == 'm':
        names = male_names
    elif gender == 'f':
        names = female_names
    elif gender == 'n':
        names = male_names + female_names

    # Losowanie pierwszych dwóch liter
    name = choice(names)[0:2]
    # Oczekiwana długość imienia
    desired_length = randint(min_length, max_mength)

    while len(name) < desired_length:
        letter = get_char(name, names)

        # Obsługa przypadku gdy nie będzie
        # żadnych pasujących liter.
        if letter:
            name += letter
        else:
            name = name[:-1]

    return name.title()

for _ in range(7):
    print(generate_name('n', 6, 10))