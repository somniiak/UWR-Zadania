#include "mniejsze.hpp"

namespace obliczenia
{
    mniejsze::mniejsze(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int mniejsze::oblicz() const {
        return arg1->oblicz() < arg2->oblicz() ? 1 : 0;
    }
    std::string mniejsze::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet() ? "(" + arg1->zapis() + ")" : arg1->zapis());
        std::string prawy = (arg2->priorytet() <= priorytet()) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + " < " + prawy;
    }
    int mniejsze::priorytet() const {
        return 5;
    }
    bool mniejsze::lewostronne() const {
        return true;
    }
}
