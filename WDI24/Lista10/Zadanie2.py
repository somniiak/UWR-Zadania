class ListItem:
    def __init__(self, value=None):
        self.val = value
        self.next = None
        self.tail = None

def output(lista):
    print('[', end='')
    while lista:
        #Lista pusta
        if not lista.val and not lista.next:
            print(lista.val, end='')
            break
        print(lista.val, end=', ' if lista.next else '')
        lista = lista.next
    print(']')

def append(lista, value):
    # Jeśli pusta
    if not lista.val and not lista.next:
        return ListItem(value)
    
    # Jeśli 1-elementowa
    elif not lista.tail:
        lista.next = ListItem(value)
        lista.tail = lista.next
    
    # Jeśli n-elementowa
    else:
        lista.tail.next = ListItem(value)
        lista.tail = lista.tail.next

    return lista

def join(left, right):
    list1_head = left.head
    list2_head = right.head
    if list1_head is None:
        return list2_head  # If the first list is empty, return the second list
    current = list1_head
    while current.next is not None:
        current = current.next
    current.next = list2_head
    return list1_head


def output_reverse(lista):
    if lista.next:
        output_reverse(lista.next)
    print(lista.val, end=', ')

def reverse(lista):
    prev = None
    current = lista
    while current:
        next_item = current.next
        current.next = prev
        prev = current
        current = next_item
    return prev



x = ListItem(5)
x = append(x, 6)
x = append(x, 4)
x = append(x, 7)

output(x)

x = reverse(x)
output(x)