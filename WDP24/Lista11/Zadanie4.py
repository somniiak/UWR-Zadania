from collections import Counter

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
    """Relacje równoważności."""
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


def dhondt(parties):
    """Metoda D’Hondta."""
    quot = []
    for res in parties:
        party, votes = res
        for n in range(1, 460 + 1):
            quot.append((votes / n, party))
    quot = sorted(quot, reverse=True)[:460]
    return Counter([v[1] for v in quot])


with open('wyniki.txt', 'r', encoding='utf-8-sig') as f:
    parties = [i.strip().split(',') for i in f.readlines()]
    parties = [(i[0], int(i[1])) for i in parties]

old_sims = [[list(j) for j in i] for i in relation(set(parties))]

new_sims = []
for sim in old_sims:
    tsim = []
    for p in sim:
        tsim.append(('-'.join(sorted([i[0] for i in p])), sum([i[1] for i in p])))
    new_sims.append(tsim)
new_sims = [dict(dhondt(sim)) for sim in new_sims]


max_party = max(parties, key=lambda x: x[1])[0]


print('\nPodpunkt A:')
res = set()
for sim in new_sims:
    for k, v in sim.items():
        if v == max(sim.values()) and max_party not in k:
            res.add(', '.join([f'{k}: {v}' for k, v in sim.items()]))
            continue
for i in res: print(i)

print('\nPodpunkt B:')
res = set()
for sim in new_sims:
    for k, v in sim.items():
        if v >= 230:
            res.add(', '.join([f'{k}: {v}' for k, v in sim.items()]))
            continue
for i in res: print(i)