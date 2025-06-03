#include "kolortransnaz.hpp"

kolortransnaz::kolortransnaz(ushort r, ushort g, ushort b, ushort a, std::string n) :
    kolor(r, g, b), kolortransparentny(r, g, b, a), kolornazwany(r, g, b, n) {}
std::ostream& operator<<(std::ostream &out, const kolortransnaz &k) {
    out << "{" << k.r << ", " << k.g << ", " << k.b << ", " << k.get_alpha() << ", " << "\"" << k.get_name() << "\"" << "}";
    return out;
}