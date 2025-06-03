#include <stdexcept>
#include "line.hpp"

Line::Line() {
    A = 1; B = 1; C = 0;
}

Line::Line(double nA, double nB, double nC) {
    if (nA == 0 && nB == 0)
        throw std::logic_error("A i B nie mogą być jednocześnie równe 0");

    else {
        A = nA;
        B = nB;
        C = nC;
    }
}

double Line::get_A() {
    return A;

}
double Line::get_B() {
    return B;
}

double Line::get_C() {
    return C;
}