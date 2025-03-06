def podzial(l,p,a):
    x=a[l]
    i=l
    j=p
    while i<j:
        while a[j]>x: j=j-1
        while a[i]<x: i=i+1
        if i<j:
            y=a[j]
            a[j]=a[i]
            a[i]=y
            i=i+1
            j=j-1
    return j

def qsort(a, l, r):
#sortuje a[l...r]
    if (l < r):
        s = podzial(l,r,a)
        qsort(a, l, s)
        qsort(a, s+1, r)
    return a

arr = [123, 454, 237, 4353, 234, 121, 239, 49, 56, 23, 232, 6567, 3434]
x = qsort(arr, 0, len(arr) - 1)
print(x, len(arr))