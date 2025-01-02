def get_powerset(start_set):
    """Zbiór potęgowy."""
    def powerset(lst):
        if not lst:
            return [[]]
        
        rest_powerset = powerset(lst[1:])

        includeFirst = [[lst[0]] + subset for subset in rest_powerset]
        excludeFirst = rest_powerset

        return includeFirst + excludeFirst

    return [set(subset) for subset in powerset(list(start_set))]


def relation(start_set):
    res = []

    def backtrack(partition, remaining_set):
        if not remaining_set:
            if sorted(list(map(list, partition))) not in [sorted(list(map(list, l))) for l in res]:
                res.append(sorted(partition))

        for subset in get_powerset(remaining_set):
            if subset and all(subset.isdisjoint(s) for s in partition):
                backtrack(partition + [subset], remaining_set - subset)

    backtrack([], start_set)

    return res


nums = {1, 2, 3, 4}
nums = relation(nums)
print(list(nums))