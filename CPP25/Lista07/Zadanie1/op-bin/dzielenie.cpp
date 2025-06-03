#include "dzielenie.hpp"

namespace obliczenia
{
    dzielenie::dzielenie(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int dzielenie::oblicz() const {
        return arg1->oblicz() / arg2->oblicz();
    }
    std::string dzielenie::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet() ? "(" + arg1->zapis() + ")" : arg1->zapis());
        std::string prawy = (arg2->priorytet() <= priorytet()) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + " / " + prawy;
    }
    int dzielenie::priorytet() const {
        return 30;
    }
    bool dzielenie::lewostronne() const {
        return true;
    }
}
