#include <iostream>

int main()
{
    int a, b, t;
    std::cin >> a >> b;

    if (a > b) {
        t = a;
        a = b;
        b = t;
    };

    for (int i = a; i <= b; i ++)
        std::cout << i << "\n";

    return 0;
}