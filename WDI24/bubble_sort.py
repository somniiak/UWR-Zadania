def bubble_sort(arr, n):
    for i in range(n):
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr

tab = [10, 9, 8, 7, 6]
n = len(tab)
tab = bubble_sort(tab, n)
print(tab)