from collections import Counter

def common_prefix(lista_slow):
    # Małe litery, usuwanie znaków białych
    lista_slow = [word.lower().strip() for word in lista_slow if word]
    if not lista_slow:
        return ""

    # Znalezienie najczęściej występującej litery na początku wyrazów
    common_letter = Counter(
        [word[0] for word in lista_slow]).most_common(1)[0]

    # Usuwanie wyrazów niezaczynających się na tą literę i usunięcie
    # pierwszej litery w reszcie (do dalszej rekurencji)
    lista_slow = [word[1:] for word in lista_slow
                    if word[0] == common_letter[0]]

    # Rekurencyjne wyszukiwanie kolejnych najczęstszych liter
    return common_letter[0] + common_prefix(lista_slow) if common_letter[1] >= 3 else ""


print(common_prefix(["Cyprian", "cyberotoman", "cynik", "ceniąc", "czule"]))