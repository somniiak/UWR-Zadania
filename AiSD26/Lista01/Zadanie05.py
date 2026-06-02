def longest_path_distance(graph):
    n = len(graph)
    indeg = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                indeg[j] += 1

    queue = [v for v in range(n) if indeg[v] == 0]
    order = []

    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in range(n):
            if graph[u][v] == 1:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)

    dist = [0] * n
    for v in order:
        for i in range(n):
            if graph[v][i] == 1:
                if dist[i] < dist[v] + 1:
                    dist[i] = dist[v] + 1

    return max(dist) + 1

def longest_path(graph):
    n = len(graph)
    indeg = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                indeg[j] += 1

    queue = [v for v in range(n) if indeg[v] == 0]
    order = []

    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in range(n):
            if graph[u][v] == 1:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)

    dist = [0] * n
    prev = [None] * n
    for v in order:
        for i in range(n):
            if graph[v][i]:
                if dist[i] < dist[v] + 1:
                    dist[i] = dist[v] + 1
                    prev[i] = v

    path = []
    t = dist.index(max(dist))
    while t is not None:
        path.insert(0, t)
        t = prev[t]

    return path


graph = [
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0],
]

print(longest_path_distance(graph))
print(longest_path(graph))
