#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>


std::vector<int64_t> rozklad(int64_t num)
{
    std::vector<int64_t> res;

    // Przypadki bazowe.
    switch (num)
    {
        case -1:
            res.push_back(-1);
            return res;
        case 0:
            res.push_back(0);
            return res;
        case 1:
            res.push_back(1);
            return res;
    }

    // Liczba ujemna. (1)
    if (num < 0)
        res.push_back(-1);

    // Dzielimy przez dwa, żeby potem
    // sprawdzać tylko liczby nieparzyste.
    // Dzielenie przez dwa trzeba wykonać
    // przed mnożeniem przez -1.
    while (num % 2 == 0)
    {
        res.push_back(2);
        num /= 2;
    }

    // Liczba ujemna. (2)
    if (num < 0)
    {
        num *= -1;
    }

    // Sprawdzamy nieparzyste dzielniki do
    // sqrt(num). Typ 'unsigned long long'
    // pozwala na sprawdzanie dużych liczb.
    for (unsigned long long i = 3; i * i <= num; i += 2)
    {
        // Liczba może występować parokrotnie. 
        while (num % i == 0)
        {
            res.push_back(i);
            num /= i;
        }
    }

    // Jeśli pozostanie liczba większa
    // od 1, to jest liczbą pierwszą.
    if (num > 1)
        res.push_back(num);

    return res;
}

// Równoważny zapis: *argv[], **argv.
int main(int argc, char *argv[])
{
    // Brak argumentów wejścia.
    if (argc == 1)
    {
        const std::string err_msg =
            "Nie podano argumentów. Liczby "
            "należy przekazać do programu "
            "poprzez argument wywołania.";

        std::cerr << err_msg << std::endl;
        return 1;
    }

    // Iteracja po argumentach.
    for (int num = 1; num < argc; num++)
    {
        int64_t val;

        // Błąd konwersji.
        // https://en.cppreference.com/w/cpp/error/invalid_argument
        try
        {
            val = std::stoll(argv[num]);
        }
        catch (const std::invalid_argument&)
        {
            std::cerr << "\"" << argv[num];
            std::cerr << "\" nie jest poprawną wartością!";
            std::cerr << std::endl; continue;
        }

        std::cout << argv[num] << " = ";
        std::vector<int64_t> res = rozklad(val);

        for (int idx = 0; idx < res.size(); idx++)
        {
            std::cout << res[idx];
            if (idx != res.size() - 1)
                std::cout << " * ";
        }

        std::cout << std::endl;
    }

    return 0;
}