#include <iostream>
#include <string>
#include <cmath>
#include "complex.hpp"
#include "polynominal.hpp"

using math::complex;
using calc::polynominal;

int main (int argc, char **argv)
{
    /* COMPLEX.HPP */
    std::cout << "\nCOMPLEX\n";
    complex comp1(21, 37);
    complex comp2(6, 9);
    std::cout << "comp1: " << comp1 << std::endl;
    std::cout << "comp2: " << comp2 << std::endl;
    std::cout << "comp1 + comp2: " << comp1 + comp2 << std::endl;
    std::cout << "comp1 - comp2: " << comp1 - comp2 << std::endl;
    std::cout << "comp1 * comp2: " << comp1 * comp2 << std::endl;
    std::cout << "comp1 / comp2: " << comp1 / comp2 << std::endl;
    std::cout << "Sprzężenie comp1: " << comp1.conjugated() << std::endl;
    complex comp3; std:: cin >> comp3;
    std::cout << "comp3: " << comp3 << std::endl;


    /* POLYNOMINAL.HPP */
    // Inicjalizacja
    std::cout << "\nPOLYNOMINAL\n";
    polynominal wielom1(5, 5);
    complex arr[] = {complex(5, 4), complex(3, 2), complex(6, 9), complex(42, 0)};
    polynominal wielom2(3, arr);
    polynominal wielom3({complex(0, 2), complex(1, 1), complex(6, 2), complex(4, 3), complex(9, 8)});
    std::cout << "wielom1: " << wielom1 << std::endl;
    std::cout << "wielom2: " << wielom2 << std::endl;
    std::cout << "wielom3: " << wielom3 << std::endl;

    // Operatory
    std::cout << "wielom2 + wielom3: " << wielom2 + wielom3 << std::endl;
    std::cout << "wielom2 - wielom3: " << wielom2 - wielom3 << std::endl;
    std::cout << "wielom2 * wielom3: " << wielom2 * wielom3 << std::endl;
    std::cout << "wielom3 * 5: " << wielom3 * 5 << std::endl;
    std::cout << "0.5 * wielom3: " << 0.5 * wielom3 << std::endl;
    std::cout << "wielom2[3]: " << wielom2[3] << std::endl; // Odczytanie współczynnika
    wielom2[3] = 1; // Nadpisanie współczynnika
    std::cout << "wielom2[3]: " << wielom2[3] << std::endl;
    std::cout << "wielom2 dla z = 1 + 3i: " << wielom2(complex(1, 3)) << std::endl; // Schemat Hornera

    // Kopiowanie, przenoszenie
    polynominal wielom4(4, 7);
    std::cout << "wielom4: " << wielom4 << std::endl;
    polynominal wielom5 = std::move(wielom4); // Przenoszenie
    std::cout << "wielom4 (przenoszenie)-> wielom5: " << wielom5 << std::endl;
    polynominal wielom6 = wielom5; // Kopiowanie
    std::cout << "wielom5 (kopiowanie)-> wielom6:" << wielom5 << ", " << wielom6 << std::endl;


    /* Wyznaczania miejsc zerowych zespolonej funkcji kwadratowej. */
    std::cout << "\nFUNKCJA KWADRATOWA\n";

    complex wsp[3] = {0}; // Tablica z współczynnikami

    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 1; j++) {
            if (j == 0) {
                std::string re;
                std::cout << "Re z^" << i << ": ";
                std::cin >> re;
                try { double tmp = std::stod(re); wsp[i].re(tmp); }
                catch (const std::invalid_argument&) {
                    std::cerr << "Podano niepoprawną wartością! Spróbuj ponownie." << std::endl;
                    std::cin.clear(); std::cin.ignore(10000,'\n'); j--;
                }
            }
            if (j == 1) {
                std::string im;
                std::cout << "Im z^" << i << ": ";
                std::cin >> im;
                try { double tmp = std::stod(im); wsp[i].im(tmp); }
                catch (const std::invalid_argument&) {
                    std::cerr << "Podano niepoprawną wartością! Spróbuj ponownie." << std::endl;
                    std::cin.clear(); std::cin.ignore(10000,'\n'); j--;
                }
            }
        }
    }

    polynominal func({wsp[0], wsp[1], wsp[2]}); // Funkcja kwadratowa
    std::cout << func << std::endl;

    complex det = func[1] * func[1] - 4 * func[0] * func[2];
    std::cout << "Delta Δ: " << det << std::endl;

    double r = sqrt(det.re() * det.re() + det.im() * det.im());
    double angle = atan2(det.im(), det.re());
    complex sdet1(
        sqrt(r) * cos(angle / 2),
        sqrt(r) * sin(angle / 2)
    );
    complex sdet2 = sdet1 * -1;
    std::cout << "Sqrt √Δ1: " << sdet1 << std::endl;
    std::cout << "Sqrt √Δ2: " << sdet2 << std::endl;

    complex z1((-1 * func[1] + sdet1) / (2 * func[2]));
    complex z2((-1 * func[1] - sdet1) / (2 * func[2]));
    std::cout << "z1: " << z1 << std::endl;
    std::cout << "z2: " << z2 << std::endl;

    return 0;
}