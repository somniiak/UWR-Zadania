#include <iostream>

#include "wyrazenie.hpp"
#include "liczba.hpp"
#include "stala.hpp"
#include "zmienna.hpp"
#include "minus.hpp"
#include "dodawanie.hpp"
#include "odejmowanie.hpp"
#include "mnozenie.hpp"
#include "dzielenie.hpp"
#include "modulo.hpp"
#include "potega.hpp"
#include "logarytm.hpp"
#include "mniejsze.hpp"
#include "wieksze.hpp"
#include "mniejsze_rowne.hpp"
#include "wieksze_rowne.hpp"
#include "rowne.hpp"
#include "rozne.hpp"

using namespace obliczenia;

int main(int argc, char **argv)
{
    zmienna::dodaj("x", 6);
    wyrazenie* w = new potega(
        new liczba(2),
        new odejmowanie(
            new dzielenie(
                new zmienna("x"),
                new liczba(3)
            ),
            new jeden()
        )
    );
    std::cout << "Wyrażenie: " << w->zapis() << std::endl;
    std::cout << "Wynik (x = 2): " << w->oblicz() << std::endl;
    zmienna::ustaw("x", 9);
    std::cout << "Wynik (x = 9): " << w->oblicz() << std::endl;
    std::cout << std::endl;
    zmienna::usun("x");
    delete w;
    zmienna::dodaj("y", 3);
    wyrazenie* v = new potega(
        new liczba(2),
        new potega(
            new liczba(2),
            new zmienna("y")
        )
    );
    std::cout << "Wyrażenie: " << v->zapis() << std::endl;
    std::cout << "Wynik (y = 3): " << v->oblicz() << std::endl;
    zmienna::ustaw("y", 4);
    std::cout << "Wynik (y = 4): " << v->oblicz() << std::endl;
    delete v;

    wyrazenie* u = new logarytm(new liczba(2), new liczba(7));
    std::cout << u->zapis() << std::endl;
    std::cout << u->oblicz() << std::endl;
    return 0;
}