#include "kolortransparentny.hpp"
#include <stdexcept>

kolortransparentny::kolortransparentny() : kolor(), alfa(255) {}
kolortransparentny::kolortransparentny(ushort red, ushort green, ushort blue, ushort value) : kolor(red, green, blue) {
    if (value < 0 || value > 255)
        throw std::out_of_range("Wartość składowej koloru poza zakresem!");
    alfa = value;
}
ushort kolortransparentny::get_alpha() const { return alfa; }
void  kolortransparentny::set_alpha(ushort value) {
    if (value < 0 || value > 255)
        throw std::out_of_range("Wartość składowej koloru poza zakresem!");
    alfa = value;
}
std::ostream& operator<<(std::ostream &out, const kolortransparentny &k) {
    out << "{" << k.r << ", " << k.g << ", " << k.b << ", " << k.get_alpha() << "}";
    return out;
}