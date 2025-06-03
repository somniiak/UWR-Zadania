#include "minus.hpp"

namespace obliczenia
{
    minus::minus(wyrazenie* w) : operator1(w) {};

    int minus::oblicz() const {
        return -arg1->oblicz();
    }
    std::string minus::zapis() const {
        return "-" + (
            arg1->priorytet() < this->priorytet() ?
            ("(" + arg1->zapis() + ")") : arg1->zapis()
        );
    }
    int minus::priorytet() const {
        return 90;
    }
    bool minus::lewostronne() const {
        return true;
    }
}
