#include "modulo.hpp"

namespace obliczenia
{
    modulo::modulo(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int modulo::oblicz() const {
        int res = arg1->oblicz() % arg2->oblicz();
        if (res < 0)
            return res + arg2->oblicz();
        else
            return res;
    }
    std::string modulo::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet() ? "(" + arg1->zapis() + ")" : arg1->zapis());
        std::string prawy = (arg2->priorytet() < priorytet() || (arg2->priorytet() == priorytet() && !lewostronne())) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + " % " + prawy;
    }
    int modulo::priorytet() const {
        return 30;
    }
    bool modulo::lewostronne() const {
        return true;
    }
}
