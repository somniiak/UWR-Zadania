class ListItem:
    def __init__(self, value=None):
        self.val = value
        self.next = None

def output(lista):
    print('[', end='')
    while lista:
        #Lista pusta
        if not lista.val and not lista.next:
            break
        print(lista.val, end=', ' if lista.next else '')
        lista = lista.next
    print(']')

def prepend(lista, value):
    # Jeśli pusta
    if not lista.val and not lista.next:
        return ListItem(value)

    # Jeśli niepusta
    else:
        nowy = ListItem(value)
        nowy.next = lista
        return nowy

def append(lista, value):
    # Jeśli pusta
    if not lista.val and not lista.next:
        return ListItem(value)
    
    # Jeśli niepusta
    current = lista
    while current.next:
        current = current.next
    current.next = ListItem(value)

    return lista

def pop(lista):
    # Jeśli pusta lub jednoelementowa
    if not lista.next:
        return ListItem(None)

    # Jeśli ma więcej elementów
    else:
        current = lista
        while current.next.next:
            current = current.next
        current.next = None
        return lista

def copy_list(lista):
        # Jeśli pusta lub jednoelementowa
        if not lista.next:
            return ListItem(lista.val)

        # Jeśli niepusta:
        copy = ListItem(lista.val)
        current_copy = copy
        current_original = lista.next

        while current_original:
            current_copy.next = ListItem(current_original.val)
            current_copy = current_copy.next
            current_original = current_original.next

        return copy

def join(left, right):
    left_copy = copy_list(left)
    right_copy = copy_list(right)

    # Jeśli lewa pusta - po złączeniu jest tylko prawa
    if not left_copy.val and not left_copy.next:
        return right_copy
    
    # Jeśli lewa niepusta
    else:
        current = left_copy
        while current.next:
            current = current.next
        current.next = right_copy
        return left_copy
    
def remove(lista, value):
    # Jeśli usuwamy wartości z przodu
    while lista and lista.val == value:
        lista = lista.next

    current = lista
    while current and current.next:
        if current.next.val == value:
            current.next = current.next.next
        else:
            current = current.next

    return lista

def output_reverse(lista):
    if lista.next:
        output_reverse(lista.next)
    print(lista.val, end=', ')

def reverse(lista):
    """Zmienne pomocnicze:
    prev – przechowuje poprzedni element (na początku None).
    current – przechowuje aktualny element, który jest przetwarzany.

    Pętla:
    Dla każdego elementu listy zapisujemy kolejny element w next_node.
    Następnie zmieniamy wskaźnik next bieżącego elementu (current) na poprzedni element (prev).
    Przesuwamy wskaźnik prev na bieżący element, a current na kolejny element zapisany w next_node.

    Końcowy wynik:
    Po zakończeniu pętli zmienna prev będzie wskazywała na nowy początek listy (odwróconą)."""
    prev = None
    current = lista
    while current:
        next_item = current.next
        current.next = prev
        prev = current
        current = next_item
    return prev


def sign(lista):
    pos_head = None
    pos_tail = None
    neg_head = None
    neg_tail = None

    current = lista
    while current:
        next_item = current.next

        if current.val >= 0:
            if pos_head is None:
                pos_head = current
                pos_tail = current
            else:
                pos_tail.next = current
                pos_tail = current
        else:
            if neg_head is None:
                neg_head = current
                neg_tail = current
            else:
                neg_tail.next = current
                neg_tail = current
    
        current.next = None  # Zrywamy link, żeby uniknąć cyklicznych odniesień
        current = next_item  # Przechodzimy do następnego elementu

    return pos_head, neg_head

x = ListItem(5)
x = append(x, 6)
x = append(x, -5)
x = append(x, 4)
x = append(x, 7)
x = append(x, -1)
x = append(x, -3)
x = append(x, -6)

output(x)

x = sign(x)
output(x[0])