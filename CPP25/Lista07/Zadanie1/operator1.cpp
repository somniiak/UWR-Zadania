#include "operator1.hpp"

namespace obliczenia
{
    operator1::operator1(wyrazenie* a) : arg1(a) {};

    operator1::~operator1() {
        delete arg1;
    }
}
