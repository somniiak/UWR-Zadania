#include <cstdio>
#include <climits>
#include <vector>
#include <algorithm>

struct HeapNode
{
    long long dist;
    int city;
};

struct MinHeap
{
    std::vector<HeapNode> array;

    bool empty() {
        return array.empty();
    }

    void push(HeapNode node) {
        array.push_back(node);

        int i = array.size() - 1;
        while(i != 0 && array[(i - 1) / 2].dist > array[i].dist) {
            std::swap(array[(i - 1) / 2], array[i]);
            i = (i - 1) / 2;
        }
    }

    HeapNode pop() {
        HeapNode root = array[0];

        array[0] = array.back();
        array.pop_back();

        if (!array.empty())
            heapify(0);

        return root;
    }

    void heapify(int i) {
        int smallest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int size = array.size();

        if (left < size && array[left].dist < array[smallest].dist)
            smallest = left;

        if (right < size && array[right].dist < array[smallest].dist)
            smallest = right;

        if (smallest != i) {
            std::swap(array[i], array[smallest]);  
            heapify(smallest);                
        }
    }
};

int countCities, countPaths, countTargets;
std::vector<std::vector<std::pair<int,int>>> graph;

std::vector<long long> dijkstra()
{
    std::vector<long long> dist(countCities + 1, LLONG_MAX);
    dist[1] = 0;

    MinHeap pq;
    pq.push({0, 1});

    while (!pq.empty()) {
        auto [d, u] = pq.pop();

        if (d > dist[u])
            continue;

        for (auto [v, w] : graph[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }

    return dist;
}

int main()
{
    scanf("%d %d %d", &countCities, &countPaths, &countTargets);
    graph.resize(countCities + 1);

    // Budujemy listę incydencji
    int a, b, d;
    for (int i = 0; i < countPaths; i++) {  
        scanf("%d %d %d", &a, &b, &d);
        graph[a].push_back({b, d});
        graph[b].push_back({a, d});
    }

    // Miasta docelowe
    std::vector<int> targets(countTargets);
    for (int i = 0; i < countTargets; i++)
        scanf("%d", &targets[i]);

    // Najkrótsze ścieżki
    std::vector<long long> dist = dijkstra();

    // Przebyty dystans
    long long totalDist = 0;

    for (int t : targets) {
        if (dist[t] == LLONG_MAX) {
            printf("NIE\n"); return 0;
        } totalDist += 2 * dist[t];
    }

    printf("%lld\n", totalDist);
    return 0;
}
