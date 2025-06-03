#include <iostream>
#include "wymierna.hpp"

using namespace obliczenia;

int main()
{
    wymierna a(69, 420);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a = wymierna(1, 2) + wymierna(3, 4);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a = wymierna(5, 6) - wymierna(7, 8);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a = wymierna(9, 10) * wymierna(11, 12);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a = wymierna(13, 14) / wymierna(15, 16);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a = wymierna(13, 14) / wymierna(15, 16);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a += wymierna(1, 2);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a -= wymierna(3, 4);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a *= wymierna(5, 6);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a /= wymierna(7, 8);
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a = -a;
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;
    a = !a;
    std::cout << a.get_licz() << "/" << a.get_mian() << std::endl;

    wymierna b(2359348, 99900); // Okres 3-liczbowy
    std::cout << b << std::endl;
    wymierna c(593, 53); // Okres 13-liczbowy
    std::cout << c << std::endl;
    wymierna d(228142, 62265); // Okres 1776-liczbowy
    std::cout << d << std::endl;
    return 0;
}