#include "punkt.hpp"

punkt::punkt() {
    x = 0; y = 0;
}

punkt::punkt(int nx, int ny) {
    x = nx; y = ny;
}

double punkt::get_x() { return x; }
double punkt::get_y() { return y; }
void punkt::set_x(int nx) { x = nx; }
void punkt::set_y(int ny) { y = ny; }