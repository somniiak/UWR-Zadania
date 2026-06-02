#include <algorithm>
#include <cstdio>
#include <vector>

// Union Find z Path halving, Union by size, wektorem do zapisywania
// aktywnych pól i licznikiem niezależnych obszarów.

struct UnionFind
{
    std::vector<int> parent, size;
    std::vector<bool> active;
    int sets = 0;

    UnionFind(int n) : parent(n), size(n, 1), active(n, false) {
        for (int i = 0; i < n; i++)
            parent[i] = i;
    }

    void activate(int idx) {
        active[idx] = true;
        sets++;
    }

    int find(int x) {
        while (x != parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        } return x;
    }

    void unite(int a, int b) {
        a = find(a);
        b = find(b);

        if (a == b)
            return;

        if (size[a] < size[b])
            std::swap(a, b);

        parent[b] = a;
        size[a] += size[b];
        sets--;
    }
};

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    // (x, y) -> x * m + y
    std::vector<int> island(n * m);
    for (int i = 0; i < n * m; i++)
        scanf("%d", &island[i]);

    int T;
    scanf("%d", &T);

    std::vector<int> t_arr(T);
    for (int i = 0; i < T; i++)
        scanf("%d", &t_arr[i]);

    // Indeksy komórek na wyspie malejąco po wysokości
    std::vector<int> cells(n * m);
    
    for (int i = 0; i < n * m; i++)
        cells[i] = i;

    std::sort(cells.begin(), cells.end(), [&](int a, int b) {
        return island[a] > island[b];
    });

    const int dx[] = {-1, 1, 0, 0};
    const int dy[] = {0, 0, -1, 1};

    UnionFind uf(n * m);
    std::vector<int> res(T, 0);
    int current = 0;

    // Dni w odwrotnej kolejności
    for (int ti = T - 1; ti >= 0; ti--) {
        while (current < n * m && island[cells[current]] > t_arr[ti]) {
            int idx = cells[current];
            int i = idx / m, j = idx % m;
            uf.activate(idx);

            for (int r = 0; r < 4; r++) {
                int ni = i + dx[r];
                int nj = j + dy[r];
                int nidx = ni * m + nj;

                if (ni >= 0 && ni < n && nj >= 0 && nj < m)
                    if (uf.active[nidx])
                        uf.unite(idx, nidx);
            } current++;
        } res[ti] = uf.sets;
    }

    for (int i = 0; i < T - 1; i++)
        printf("%d ", res[i]);
    printf("%d\n", res[T - 1]);

    return 0;
}
