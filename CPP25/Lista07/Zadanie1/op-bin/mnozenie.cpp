#include "mnozenie.hpp"

namespace obliczenia
{
    mnozenie::mnozenie(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int mnozenie::oblicz() const {
        return arg1->oblicz() * arg2->oblicz();
    }
    std::string mnozenie::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet() ? "(" + arg1->zapis() + ")" : arg1->zapis());
        std::string prawy = (arg2->priorytet() < priorytet() || (arg2->priorytet() == priorytet() && !lewostronne())) ? ("(" + arg2->zapis() + ")") : arg2->zapis();
        return lewy + " * " + prawy;
    }
    int mnozenie::priorytet() const {
        return 30;
    }
    bool mnozenie::lewostronne() const {
        return true;
    }
}
