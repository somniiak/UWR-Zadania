# Artur Dzido
# Zadanie 4, Lista 1
# (Python 3.13.2)


lista = ('jeden', ('dwa', ('trzy', None)))

# Funkcyjnie
def fun_func(lista, funkcja):
    if not lista:
        return None

    left = lista[0]
    right = lista[1]

    if funkcja(left):
        return (left, fun_func(right, funkcja))

    else:
        return (fun_func(right[1], funkcja))

'''
#Przykład
def isEven(word):
    if len(word) % 2:
        return False
    return True

x = fun_func(lista, isEven)
print(x)
'''


# Proceduralnie
def pro_func(lista, funkcja):
    tmp = lista
    cnt = 0
    while tmp:
        tmp = tmp[1]
        cnt += 1

    cur = lista
    arr = [''] * cnt

    res = None
    for idx in range(cnt):
        arr[cnt - idx - 1] = cur[0]
        cur = cur[1]

    res = None
    for idx in range(cnt):
        if funkcja(arr[idx]):
            res = (arr[idx], res)

    return res


'''
#Przykład
def isEven(word):
    if len(word) % 2:
        return False
    return True

x = pro_func(lista, isEven)
print(x)
'''