#include "wieksze.hpp"

namespace obliczenia
{
    wieksze::wieksze(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int wieksze::oblicz() const {
        return arg1->oblicz() > arg2->oblicz() ? 1 : 0;
    }
    std::string wieksze::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet() ? "(" + arg1->zapis() + ")" : arg1->zapis());
        std::string prawy = (arg2->priorytet() <= priorytet()) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + " > " + prawy;
    }
    int wieksze::priorytet() const {
        return 5;
    }
    bool wieksze::lewostronne() const {
        return true;
    }
}
