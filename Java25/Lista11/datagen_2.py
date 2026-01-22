from random import randint, choice, random

lipsum = [
    'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing',
    'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore',
    'et', 'dolore', 'magna', 'aliqua', 'ut', 'enim', 'ad', 'minim', 'veniam',
    'quis', 'nostrud', 'exercitation', 'ullamco', 'laboris', 'nisi', 'ut',
    'aliquip', 'ex', 'ea', 'commodo', 'consequat',
]

with open('sample.txt', 'w+') as f:
    for _ in range(500):

        r = random

        # Ilość liczb w linii
        nums = choice([
            [],
            [r() * 100],
            [r() * 100, r() * 100],
            [r() * 100, r() * 100, r() * 100],
            [r() * 100, r() * 100, r() * 100, r() * 100] 
        ])

        # Niektóre całkowite
        nums = [
            str(int(num)) if choice([True, False])
            else f'{num:.4f}' for num in nums
        ]

        line = ' '.join(nums)

        # Czy zawiera komentarz
        if choice([True, False]):
            start = randint(0, len(lipsum) - 1)
            end = randint(start + 1, len(lipsum))

            line += '//' + ' '.join(lipsum[start:end])
        
        # Znaki białe (początek)
        for i in range(randint(0, 7)):
            line = choice([' ', '\t']) + line

        # Znaki białe (koniec)
        for i in range(randint(0, 7)):
            line = line + choice([' ', '\t'])

        f.write(line + "\n")