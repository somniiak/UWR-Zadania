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

def merge(left, right):
    # Ustalamy nową głowę listy w zależności od mniejszego pierwszego elementu
    if left is None:
        return right
    if right is None:
        return left

    if left.val <= right.val:
        merged_head = left
        left = left.next
    else:
        merged_head = right
        right = right.next
    
    
    # Ustawiamy aktualny element na początek scalonej listy
    current = merged_head
    
    # Przechodzimy przez obie listy i łączymy elementy w porządku
    while left is not None and right is not None:
        if left.val <= right.val:
            current.next = left
            left = left.next
        else:
            current.next = right
            right = right.next

        current = current.next

    # Dołączamy pozostałe elementy z jednej z list (jeśli są) (i tak są posortowane)
    if left is not None:
        current.next = left
    if right is not None:
        current.next = right
    
    return merged_head


x = ListItem(3)
x = append(x, 4)
x = append(x, 8)
x = append(x, 9)

y = ListItem(4)
y = append(y, 5)
y = append(y, 7)
y = append(y, 9)
y = append(y, 10)

output(x)
output(y)
merge(x, y)
output(x)