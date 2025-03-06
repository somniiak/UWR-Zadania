from wdi import *

steps = 0

def min(arr, start, stop):
    global steps
    if stop == 1:
        return arr[0]
    else:
        l = n // 2

        arr_l = Array(l)
        for val in range(l):
            arr_l[val] = arr[val]
        
        arr_p = Array(n - l)
        for val in range(n - l):
            arr_p[val] = arr[val + l]

        arr_l = min(arr_l, 0, l)
        arr_p = min(arr_p, n - l, stop)
        steps+=1
        if arr_l < arr_p:
            return arr_l
        else:
            return arr_p

arr = [123, 454, 237, 4353, 234, 121, 239, 49, 56, 23, 232, 6567, 3434]
x = min(arr, 0, len(arr))
print(x, len(arr), steps)