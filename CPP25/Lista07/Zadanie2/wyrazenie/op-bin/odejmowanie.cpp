#include "odejmowanie.hpp"

namespace obliczenia
{
    odejmowanie::odejmowanie(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int odejmowanie::oblicz() const {
        return arg1->oblicz() - arg2->oblicz();
    }
    std::string odejmowanie::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet() ? "(" + arg1->zapis() + ")" : arg1->zapis());
        std::string prawy = (arg2->priorytet() <= priorytet()) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + " - " + prawy;
    }
    int odejmowanie::priorytet() const {
        return 10;
    }
    bool odejmowanie::lewostronne() const {
        return true;
    }
}
