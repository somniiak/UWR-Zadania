from datetime import datetime, timedelta
from random import randint, choice

addresses = ['.'.join([
        str(randint(0, 255)) for _ in range(4)
    ]) for _ in range(150)]

def get_time() -> str:
    return datetime.now().strftime('%H:%M:%S')

def inc_time(i) -> str:
    return (datetime.now() + timedelta(seconds=i)).strftime('%H:%M:%S')

def get_ip() -> str:
    return choice(addresses)

def get_file() -> str:
    return choice([
        '/TheApplication/WebResource.axd',
        '/Odpowiedzi/Kolokwium_z_logiki.pdf',
        '/Listy/MDL_05.pdf',
        '/Odpowiedzi/EgzaminAISD2025.pdf',
        '/Files/Sample.txt',
        '/Private/vbucks.py',
        '/robots.txt',
    ])

with open('server.log', 'a', encoding='utf-8') as f:
    for i in range(99999):
        f.write(
            inc_time(i) + ' ' + get_ip() + ' GET ' + get_file() + ' 200\n'
        )
