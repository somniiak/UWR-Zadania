from heapq import heapify, heappush, heappop

# https://stackoverflow.com/q/21134720
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/
#
# 1. Use a Min-Heap and insert the first elements from `K` lists
# 2. Remove the the min element and add the next element from the same list
# 3. Simultaneously track the max and min value so that we can calculate the minimum range
#
# Czas: O(n * log(k)), gdzie n to długość najdłuższej listy, a k to liczba list.
# Pamięć: O(k), bo kopiec zawiera po jednym elemencie z każdej listy.

def minimal_r(lists):
    k = len(lists)

    max_val = 0
    heap = []

    for i in range(k):
        max_val = max(max_val, lists[i][0])
        heappush(heap, (lists[i][0], i, 0))

    best_r = float('inf')
    best_a = 0

    while heap:
        cur_min, list_idx, i = heappop(heap)
        r = max_val - cur_min

        if r < best_r:
            best_r = r
            best_a = cur_min

        # Jeśli znaleźliśmy przedział o długości 0, nie da się znaleźć mniejszego.
        # Jeśli aktualna lista nie ma kolejnego elementu, nie możemy kontynuować.
        if best_r == 0 or i + 1 >= len(lists[list_idx]):
            break

        # Pobieramy następny element z tej samej listy i wkładamy go do kopca.
        # Dzięki temu kopiec nadal zawiera po jednym elemencie z każdej listy.
        nxt = lists[list_idx][i + 1]
        heappush(heap, (nxt, list_idx, i + 1))

        # Aktualizujemy największy element w bieżącym zestawie, bo nxt może być nowym max_val.
        max_val = max(max_val, nxt)

    return best_a, best_r

lists = [
    [4, 5, 8],
    [2, 9, 12],
    [4, 6, 14],
]

a, r = minimal_r(lists)

print(f"a={a}, r={r}, interval=[{a}, {a+r}]")