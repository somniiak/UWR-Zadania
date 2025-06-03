#include <iostream>
#include "punkt.hpp"
#include "kolejka.hpp"

void wypisz(kolejka kol)
{
    std::cout << "{";
    while(kol.dlugosc()) {
        punkt pun = kol.usun();
        std::cout << "(" << pun.get_x() << ", " << pun.get_y() << ")";
        if (kol.dlugosc())
            std::cout << ", ";
    }
    std::cout << "}" << std::endl;
}

int main(int argc, char **argv)
{
    // Kolejka z zadaną pojemnością
    std::cout << "\n";
    kolejka alfa(4);
    alfa.wstaw(punkt(2, 5));
    alfa.wstaw(punkt(4, 10));
    alfa.wstaw(punkt(4, 1));
    alfa.wstaw(punkt(10, 1));
    wypisz(alfa);
    // alfa.wstaw(punkt(6, 9)); // Błąd: dodawanie do pełnej kolejki

    // Kolejka bez arugmentów
    std::cout << "\n";
    kolejka beta;
    beta.wstaw(punkt(10, 2));
    std::cout << "Dlugość kolejki: " << beta.dlugosc() << std::endl;

    // Kolejka z listą inicjalizacyjną
    std::cout << "\n";
    kolejka gamma{punkt(2, 1), punkt(3, 7), punkt(4, 2), punkt(0, 0)};
    wypisz(gamma);
    std::cout << "Dlugość kolejki: " << gamma.dlugosc() << std::endl;
    punkt x = gamma.usun(); // Zdejmujemy element z kolejki
    std::cout << "Zdjęty element: (" << x.get_x() << ", " << x.get_y() << ").\n";
    wypisz(gamma);
    std::cout << "Dlugość kolejki: " << gamma.dlugosc() << std::endl; 

    // Kopiowanie kolejki
    std::cout << "\n";
    kolejka delta = gamma;
    wypisz(gamma);
    wypisz(delta);

    // Przeniesienie kolejki
    std::cout << "\n";
    kolejka epsilon = std::move(gamma);
    wypisz(epsilon);
    wypisz(gamma);

    return 0;
}