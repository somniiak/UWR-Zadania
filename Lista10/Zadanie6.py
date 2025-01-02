from random import choice, randint
from re import finditer

with open('imiona_meskie.txt', 'r', encoding='utf8') as f:
    male_names = [f'^^{name.strip()}$' for name in f.readlines()]

with open('imiona_zenskie.txt', 'r', encoding='utf8') as f:
    female_names = [f'^^{name.strip()}$' for name in f.readlines()]

def get_char(current, names):
    """Generowanie litery do dodanie."""
    letters = {l: 0 for l in 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'}
    postfix = current[-2:] # Końcówka
    i2 = postfix[0] # Przedostatnia litera
    i1 = postfix[1] # Ostatnia litera

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
    name = choice(names)[2:4]
    # Oczekiwana długość imienia
    desired_length = randint(min_length, max_mength)
    # Obecna długość imienia
    current_length = 2

    while current_length < desired_length:
        letter = get_char(name, names)

        # Obsługa rzadkiego przypadku gdy
        # nie będzie żadnych pasujących liter.
        if letter:
            name += get_char(name, names)
            current_length += 1
        else:
            name = name[:-1] 
            current_length -= 1

    return name.title()

imie = generate_name('f', 5, 7)
print(imie)