#include <cstdio>
#include <vector>
#include <algorithm>

int main() {
    int size;
    scanf("%d", &size);

    int total = 0;
    std::vector<int> nums(size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &nums[i]);
        total += nums[i];
    }

    std::vector<int> dp(total + 1, -1);
    dp[0] = 0;

    for (int r : nums) {
        std::vector<int> new_dp = dp;

        for (int d = 0; d <= total; d++) {
            int current = dp[d];

            if (current == -1) continue;

            // Pomijamy klocek
            new_dp[d] = std::max(new_dp[d], current);

            // Dodajemy do wyższej wieży
            if (d + r <= total)
                new_dp[d + r] = std::max(new_dp[d + r], current + r);

            // Dodajemy do niższej wieży (która może stać się wyższą)
            int nd = std::abs(d - r);
            new_dp[nd] = std::max(new_dp[nd], current + r);
        }

        dp = new_dp;
    }

    if (dp[0] > 0)
        printf("TAK\n%d\n", dp[0] / 2);
    else {
        for (int d = 1; d <= total; d++) {
            if (dp[d] > d) {
                printf("NIE\n%d\n", d);
                break;
            }
        }
    }

    return 0;
}
