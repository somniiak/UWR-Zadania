n = int(input())
g = [1, 1, 1, 0]

for i in range(n - 2):
    g[3] = g[0] + g[1] + g[2]
    g[0] = g[1]
    g[1] = g[2]
    g[2] = g[3]

print(g[3])