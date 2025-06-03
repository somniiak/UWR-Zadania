#include <stdexcept>
#include <cmath>
#include "piksel.hpp"

piksel::piksel() : x(0), y(0) {}
piksel::piksel(int nx, int ny) {
    if (nx < 0 || nx >= screen_width || ny < 0 || ny >= screen_height)
        throw std::out_of_range("Współrzędne poza wymiarem ekranu!");
    x = nx; y = ny;
}
void piksel::set_x(int nx) {
    if (nx < 0 || nx > screen_width)
        throw std::out_of_range("Współrzędne poza wymiarem ekranu!");
    x = nx;
}
void piksel::set_y(int ny) {
    if (ny < 0 || ny > screen_height)
        throw std::out_of_range("Współrzędne poza wymiarem ekranu!");
    y = ny;
}
int piksel::get_x() const { return x; }
int piksel::get_y() const { return y; }
int piksel::distance_left() { return x; }
int piksel::distance_right() { return screen_width - x - 1; }
int piksel::distance_top() { return y; }
int piksel::distance_bottom() { return screen_height - y - 1 ;}
double piksel::distance(const piksel* p1, const piksel* p2) {
    if (!p1 || !p2) throw std::invalid_argument("Przekazano pusty wskaźnik");
    return std::sqrt(std::pow(p1->x + p2->x, 2) + std::pow(p1->y + p2->y, 2));
}
double piksel::distance(const piksel& p1, const piksel& p2) {
    return std::sqrt(std::pow(p1.x + p2.x, 2) + std::pow(p1.y + p2.y, 2));
}
std::ostream& operator<<(std::ostream &out, const piksel &p) {
    out << "{X: " << p.get_x() << ", Y: " << p.get_y() << "}";
    return out;
}