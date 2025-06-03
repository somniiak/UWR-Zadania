#include "operator2.hpp"

namespace obliczenia
{
    operator2::operator2(wyrazenie* a, wyrazenie* b) : operator1(a), arg2(b) {};

    operator2::~operator2() {
        delete arg2;
    }
}
