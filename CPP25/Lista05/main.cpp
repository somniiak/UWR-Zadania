#include <iostream>
#include "kolor.hpp"
#include "kolortransparentny.hpp"
#include "kolornazwany.hpp"
#include "kolortransnaz.hpp"
#include "piksel.hpp"
#include "pikselkolorowy.hpp"


int main(int argc, char **argv)
{
    // KOLOR.HPP
    std::cout << "\nKlasa kolor:\n";
    kolor k1(4, 2, 0);
    std::cout << k1 << std::endl;
    k1.set_r(69);
    k1.set_g(96);
    k1.set_b(120);
    std::cout << k1 << std::endl;
    k1.darken(0.2);
    std::cout << k1 << "- ściemniono" << std::endl;
    k1.lighten(0.45);
    std::cout << k1 << "- rozjaśniono" << std::endl;
    kolor k2(76, 245, 179);
    kolor k3 = kolor::mix(k1, k2);
    std::cout << "Mieszam kolory " << k1 << " i " << k2 << ": " << k3 << std::endl;

    // KOLORTRANSPARENTNY.HPP
    std::cout << "\nKlasa kolor transparentny:\n";
    kolortransparentny kt1(4, 6, 120, 200);
    std::cout << kt1 << std::endl;
    kt1.lighten(0.7);
    std::cout << kt1 << std::endl;

    // KOLORTRANSNAZWANY.HPP
    std::cout << "\nKlasa kolor nazwany:\n";
    kolornazwany kn1(66, 33, 99, "rebeccapurple");
    std::cout << kn1 << std::endl;
    kn1.set_r(128);
    kn1.set_g(0);
    kn1.set_b(0);
    kn1.set_name("maroon");
    std::cout << kn1 << std::endl;

    // KOLORTRANSNAZ.HPP
    std::cout << "\nKlasa kolor nazwany transparentny:\n";
    kolortransnaz ktn1(1, 2, 4, 255, "nazwajeden");
    std::cout << ktn1 << std::endl;
    ktn1.set_alpha(0);
    ktn1.set_name("przezroczysty");
    std::cout << ktn1 << std::endl;

    // PIKSEL.HPP
    std::cout << "\nKlasa piksel:\n";
    piksel p1(21, 37);
    std::cout << p1 << std::endl;
    p1.set_x(6);
    p1.set_y(9);
    std::cout << p1 << std::endl;
    std::cout << "Odległość od lewej krawędzi: " << p1.distance_left() << std::endl;
    std::cout << "Odległość od dolnej krawędzi: " << p1.distance_bottom() << std::endl;
    piksel p2(1000, 670);
    std::cout << "Odległość pomiędzy pikselami " << p1 << " oraz " << p2 << ": " << piksel::distance(p1, p2) << " (referencja)\n";
    std::cout << "Odległość pomiędzy pikselami " << p1 << " oraz " << p2 << ": " << piksel::distance(&p1, &p2) << " (wskaźniki)\n";

    // PIKSELKOLOROWY.HPP
    std::cout << "\nKlasa piksel kolorowy:\n";
    pikselkolorowy pk1(3, 29, 4, 6, 8);
    std::cout << pk1 << std::endl;
    pk1.shift_by(200, 568);
    std::cout << pk1 << " (przesunięto o wektor)" << std::endl;
    return 0;
}