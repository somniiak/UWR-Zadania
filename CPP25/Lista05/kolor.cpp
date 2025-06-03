#include <stdexcept>
#include "kolor.hpp"

kolor::kolor() : r(0), g(0), b(0) {}
kolor::kolor(ushort red, ushort green, ushort blue) {
    if (red < 0 || red > 255 || green < 0 || green > 255 || blue < 0 || blue > 255)
        throw std::out_of_range("Wartość składowej koloru poza zakresem!");
    r = red; g = green; b = blue;
}
ushort kolor::get_r() const { return r; }
ushort kolor::get_g() const { return g; }
ushort kolor::get_b() const { return b; }
void kolor::set_r(ushort red) {
    if (red < 0 || red > 255)
        throw std::out_of_range("Wartość składowej koloru poza zakresem!");
    r = red;
}
void kolor::set_g(ushort green) {
    if (green < 0 || green > 255)
        throw std::out_of_range("Wartość składowej koloru poza zakresem!");
    g = green;
}
void kolor::set_b(ushort blue) {
    if (blue < 0 || blue > 255)
        throw std::out_of_range("Wartość składowej koloru poza zakresem!");
    b = blue;
}
void kolor::darken(float value) {
    if (value < 0 || value > 1)
        throw std::out_of_range("Niepoprawna wartośc. Podaj wartość z zakresu od 0 do 1.");
    // Ściemniamy kolor redukując wartość każdej składowej
    r = static_cast<ushort>(r * value);
    g = static_cast<ushort>(g * value);
    b = static_cast<ushort>(b * value);
}
void kolor::lighten(float value) {
    if (value < 0 || value > 1)
        throw std::out_of_range("Niepoprawna wartośc. Podaj wartość z zakresu od 0 do 1.");
    // Rozjaśniamy kolor skalując wartość każdej składowej względem 255
    r = static_cast<ushort>(r + (255 - r) * value);
    g = static_cast<ushort>(g + (255 - g) * value);
    b = static_cast<ushort>(b + (255 - b) * value);
}
kolor kolor::mix(const kolor& k1, const kolor& k2) {
    ushort avg_r = static_cast<ushort>((k1.r + k2.r) / 2);
    ushort avg_g = static_cast<ushort>((k1.g + k2.g) / 2);
    ushort avg_b = static_cast<ushort>((k1.b + k2.b) / 2);
    return kolor(avg_r, avg_g, avg_b); 
}
std::ostream& operator<<(std::ostream &out, const kolor &k) {
    out << "{" << k.r << ", " << k.g << ", " << k.b << "}";
    return out;
}