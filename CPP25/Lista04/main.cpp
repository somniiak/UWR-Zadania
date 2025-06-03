#include <iostream>
#include "wielom.hpp"


int main(int argc, char **argv)
{
    //wielom w1(7, 0); // Błąd: 0 na końcu listy
    wielom w1(7, 4);
    std::cout << w1 << std::endl;
    wielom w2({0, -2, 0, 0, 0, 2});
    // wielom w2({1, 2, 3, 5, 0}); // Błąd: 0 na końcu listy
    std::cout << w2 << std::endl;
    double wsp1[] = {23, 43, 43, 12};
    wielom wp(3, wsp1);
    std::cout << wp << std::endl;

    //Operatory
    wielom w3 = w1 + w2; std::cout << w3 << std::endl;
    w3 = w1 * w2; std::cout << w3 << std::endl;
    w3 = w1 - w2; std::cout << w3 << std::endl;
    w3 = 5 * w2; std::cout << w3 << std::endl;
    wielom w4({4, 2, 0, 2, 1, 3, 7});
    w3 -= w4 ; std::cout << w3 << std::endl;
    w3 *= 6.9 ; std::cout << w3 << std::endl;
    w3 += w4 ; std::cout << w3 << std::endl;
    w2 *= w1;
    std::cout << w2 << std::endl;
    w1 *= w2;
    std::cout << w2 << std::endl;
    std::cout << "w2[3]: " << w2[3] << std::endl; // Odczytanie współczynnika
    w2[3] = 1; // Nadpisanie współczynnika
    std::cout << "w2[3]: " << w2[3] << std::endl;
    std::cout << "w2 dla x = 2: " << w2(2) << std::endl; // Schemat Hornera

    // Wejście
    wielom w5(4, 7);
    std::cin >> w5;
    std::cout << w5 << std::endl;

    // Kopiowanie, przenoszenie
    wielom w6 = std::move(w5); // Przenoszenie
    std::cout << w6 << std::endl;
    wielom w7 = w6; // Kopiowanie
    std::cout << w6 << std::endl; 
    std::cout << w7 << std::endl;
    return 0;
}