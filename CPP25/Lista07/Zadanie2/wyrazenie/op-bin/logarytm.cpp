#include "logarytm.hpp"

namespace obliczenia
{
    logarytm::logarytm(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int logarytm::oblicz() const {
        int base = arg1->oblicz();
        int num = arg2->oblicz();
        if (base <= 1 || num <= 0)
            throw std::runtime_error("Błędne dane do logarytmu dyskretnego.");
        int res = 0, exp = 1;
        while (exp < num) {
            exp *= base;
            res++;
        }
        if (exp == num)
            return res;
        else
            return res - 1;
    }
    std::string logarytm::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet()) ? "(" + arg1->zapis() + ")" : arg1->zapis();
        std::string prawy = (arg2->priorytet() <= priorytet()) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + "_" + prawy;
    }
    int logarytm::priorytet() const {
        return 50;
    }
    bool logarytm::lewostronne() const {
        return false;
    }
}
