#include "potega.hpp"

namespace obliczenia
{
    potega::potega(wyrazenie* a, wyrazenie* b) : operator2(a, b) {};

    int potega::oblicz() const {
        int base = arg1->oblicz();
        int exp = arg2->oblicz();
        
        if (exp < 0) {
            throw std::runtime_error("Wykładnik potęgi nie może być ujemny");
        }

        int res = 1;
        
        while (exp > 0) {
            if (exp % 2) {
                if ((base > 0 && res > INT_MAX / base) || 
                    (base < 0 && res < INT_MIN / base)) {
                    throw std::overflow_error("Przepełnienie przy potęgowaniu");
                }
                res *= base;
            }
            exp /= 2;
            if (exp > 0) {
                if ((base > 0 && base > INT_MAX / base) || 
                    (base < 0 && base < INT_MIN / -base)) {
                    throw std::overflow_error("Przepełnienie przy potęgowaniu");
                }
                base *= base;
            }
        }
        
        return res;
    }
    std::string potega::zapis() const {
        std::string lewy = (arg1->priorytet() < priorytet()) ? "(" + arg1->zapis() + ")" : arg1->zapis();
        std::string prawy = (arg2->priorytet() <= priorytet()) ? "(" + arg2->zapis() + ")" : arg2->zapis();
        return lewy + " ^ " + prawy;
    }
    int potega::priorytet() const {
        return 50;
    }
    bool potega::lewostronne() const {
        return false;
    }
}
