#include "dodawanie.hpp"

namespace obliczenia
{
    dodawanie::dodawanie(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int dodawanie::oblicz() const {
        return arg1->oblicz() + arg2->oblicz();
    }
    std::string dodawanie::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet() ? "(" + arg1->zapis() + ")" : arg1->zapis());
        std::string prawy = (arg2->priorytet() < priorytet() || (arg2->priorytet() == priorytet() && !lewostronne())) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + " + " + prawy;
    }
    int dodawanie::priorytet() const {
        return 10;
    }
    bool dodawanie::lewostronne() const {
        return true;
    }
}
