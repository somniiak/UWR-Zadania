#include <cstdio>
#include <queue>

#define MAXN 2001
#define MAXM 2003
#define ushort unsigned short

int height, width;
char BOARD[MAXN][MAXM];
bool VISITED[MAXN][MAXM];

void printBoard()
{
    printf("\n");
    for (int i = 0; i < height; i++)
        printf("%s", BOARD[i]);
    printf("\n");
}

bool hasPaintedEdge(char c, char dir)
{
    switch (dir) {
        case 'l': return c == 'B' || c == 'C' || c == 'F';
        case 'r': return c == 'D' || c == 'E' || c == 'F';
        case 'u': return c == 'C' || c == 'D' || c == 'F';
        case 'd': return c == 'B' || c == 'E' || c == 'F';
    } return false;
}

bool isConnected(char fst, char snd, char dir)
{
    char opposite;

    switch (dir) {
        case 'l': opposite = 'r'; break;
        case 'r': opposite = 'l'; break;
        case 'u': opposite = 'd'; break;
        case 'd': opposite = 'u'; break;
    }

    return hasPaintedEdge(fst, dir) && hasPaintedEdge(snd, opposite);
}

void BFS(int i, int j)
{
    std::queue<std::pair<ushort,ushort>> q;
    VISITED[i][j] = true;
    q.push({i, j});

    // Sprawdzamy sąsiadów:
    // góra, dół, lewo, prawo
    int di[] = {-1, 1, 0, 0};
    int dj[] = {0, 0, -1, 1};
    char dirs[] = {'u', 'd', 'l', 'r'};

    while (!q.empty()) {
        std::pair<ushort, ushort> front = q.front(); q.pop();
        int ci = front.first;
        int cj = front.second;

        for (int d = 0; d < 4; d++) {
            int ni = ci + di[d];
            int nj = cj + dj[d];

            if (ni < 0 || nj < 0 || ni >= height ||  nj >= width)
                continue;
            if (VISITED[ni][nj] || BOARD[ni][nj] == 'A')
                continue;
            if (!isConnected(BOARD[ci][cj], BOARD[ni][nj], dirs[d]))
                continue;

            VISITED[ni][nj] = true;
            q.push({ni, nj});
        }
    }
}

int main()
{
    scanf("%d %d\n", &height, &width);

    // width + 2 na znaki '\n' i '\0' bo się wysypie
    for (int i = 0; i < height; i++)
        fgets(BOARD[i], width + 2, stdin);

    int count = 0;

    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
            if (!VISITED[i][j] && BOARD[i][j] != 'A') {
                BFS(i, j);
                count++;
            }

    //printBoard();
    printf("%d\n", count);

    return 0;
}
