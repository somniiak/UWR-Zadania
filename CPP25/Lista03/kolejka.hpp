#ifndef KOLEJKA_H
#define KOLEJKA_H

#include "punkt.hpp"
#include <initializer_list>

class kolejka
{
    private:
        int pojemnosc, pocz = 0, ile = 0;
        punkt* tab;

    public:
        kolejka(); // Konstruktor bezargumentowy (i delegatowy)
        kolejka(int s); // Konstruktor z określoną pojemnością
        kolejka(std::initializer_list<punkt> lista); // Konstruktor z listą inicjalizacyjną
        kolejka(const kolejka& kol); // Konstruktor kopiujący
        kolejka(kolejka&& kol); // Konstruktor przenoszący
        kolejka& operator=(const kolejka& kol); // Operator przypisania kopiujący
        kolejka& operator=(kolejka&& kol); // Operator przypisania przenoszący
        ~kolejka(); // Destruktor
        void wstaw(punkt pun);
        punkt usun();
        punkt zprzodu();
        int dlugosc();
};

#endif