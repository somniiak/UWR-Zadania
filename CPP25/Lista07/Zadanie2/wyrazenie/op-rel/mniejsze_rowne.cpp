#include "mniejsze_rowne.hpp"

namespace obliczenia
{
    mniejsze_rowne::mniejsze_rowne(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int mniejsze_rowne::oblicz() const {
        return arg1->oblicz() <= arg2->oblicz() ? 1 : 0;
    }
    std::string mniejsze_rowne::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet() ? "(" + arg1->zapis() + ")" : arg1->zapis());
        std::string prawy = (arg2->priorytet() <= priorytet()) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + " <= " + prawy;
    }
    int mniejsze_rowne::priorytet() const {
        return 5;
    }
    bool mniejsze_rowne::lewostronne() const {
        return true;
    }
}
