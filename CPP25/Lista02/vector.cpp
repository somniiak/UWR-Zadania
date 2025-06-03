#include <utility>
#include "vector.hpp"

Vector::Vector() {
    dx = 0; dy = 0;
}

Vector::Vector(double nx = 0, double ny = 0) {
    dx = nx; dy = ny;
}

void Vector::set_size(double nx, double ny) {
    dx = nx; dy = ny;
}

std::pair<double, double> Vector::get_size() {
    return {dx, dy};
}