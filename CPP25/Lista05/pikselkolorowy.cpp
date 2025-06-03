#include "pikselkolorowy.hpp"
#include <stdexcept>

pikselkolorowy::pikselkolorowy() : piksel(0, 0), kolor(0, 0, 0) {}
pikselkolorowy::pikselkolorowy(int nx, int ny, ushort r, ushort g, ushort b) : piksel(nx, ny), kolor(r, g, b) {}
void pikselkolorowy::shift_by(int dx, int dy) {
    int nx = get_x() + dx;
    int ny = get_y() + dy;
    if (nx < 0 || nx >= screen_width || ny < 0 || ny >= screen_height)
        throw std::out_of_range("Współrzędne poza wymiarem ekranu!");
    set_x(nx); set_y(ny);
}
std::ostream& operator<<(std::ostream &out, const pikselkolorowy &p) {
    out << "{X: " << p.get_x() << ", Y: " << p.get_y() << ", RGB: (" << p.get_r() << ", " << p.get_g() << ", " << p.get_b() << ")}";
    return out;
}