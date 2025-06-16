# Artur Dzido
# Zadanie 3, Lista 1
# (Python 3.13.2)


lista = ('jeden', ('dwa', ('trzy', None)))

# Funkcyjnie
def fun_func(lista, funkcja):
    if not lista:
        return None

    left = lista[0]
    right = lista[1]

    return (
        funkcja(left), fun_func(right, funkcja)
        )

'''
#Przykład
def funk(word):
    return word.title()[::-1]

x = fun_func(lista, funk)
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
        arr[cnt - idx - 1] = funkcja(cur[0])
        cur = cur[1]

    res = None
    for idx in range(cnt):
        res = (arr[idx], res)

    return res

'''
#Przykład
def funk(word):
    return word.title()[::-1]

x = pro_func(lista, funk)
print(x)
'''