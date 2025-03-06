alpha = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'

def caesar(s, k):
    """Szyfr cezara, k-przesunięć."""
    k %= len(alpha)
    dic = {k: v for k, v in zip(alpha + alpha.upper(), alpha[k:] + alpha[:k] + alpha[k:].upper() + alpha[:k].upper())}
    return ''.join([dic[l] if l in dic else l for l in s])


sample = 'Wyście sobie, a my sobie, każden sobie rzepkę skrobie.' # S. Wyspiański - "Wesele"
secret = caesar(sample, 6)
print(secret)