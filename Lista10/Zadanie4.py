def powerset(lst):
    if not lst:
        return [[]]
    
    rest_powerset = powerset(lst[1:])

    includeFirst = [[lst[0]] + subset for subset in rest_powerset]
    excludeFirst = rest_powerset

    return includeFirst + excludeFirst

def sum_powerset(lst):
    if not lst:
        return {0}
    
    rest_powerset = sum_powerset(lst[1:])

    includeFirst = {lst[0] + subset for subset in rest_powerset}
    excludeFirst = rest_powerset

    return includeFirst | excludeFirst

def gen_subsets(a, b, n):
    if not n:
        return [[]]

    start = [i for i in range(a, b + 1)]
    iterables = len(start) - n + 1

    subsets = []
    for idx in range(iterables):
        for idy in gen_subsets(start[idx], b, n - 1):
            subsets.append([start[idx]] + idy)

    return subsets

numbers = sum_powerset([1,2,3,100])
print(numbers)

numbers = gen_subsets(3, 12, 6)
#print(numbers)