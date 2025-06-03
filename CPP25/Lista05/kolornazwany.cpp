#include "kolornazwany.hpp"
#include <stdexcept>

kolornazwany::kolornazwany() : kolor(0, 0, 0), nazwa("") {}
kolornazwany::kolornazwany(ushort red, ushort green, ushort blue, std::string value) : kolor(red, green, blue) {
    for (char c : value) {
        if (!islower(c) || !isalnum(c))
            throw std::invalid_argument("Nazwa ma się składać tylko z małych liter alfabetu angielskiego!");
        }
    nazwa = value;
}
std::string kolornazwany::get_name() const { return nazwa; };
void kolornazwany::set_name(std::string value) {
    for (char c : value) {
        if (!islower(c) || !isalnum(c))
            throw std::invalid_argument("Nazwa ma się składać tylko z małych liter alfabetu angielskiego!");
        }
    nazwa = value;
}
std::ostream& operator<<(std::ostream &out, const kolornazwany &k) {
    out << "{" << k.r << ", " << k.g << ", " << k.b << ", " << "\"" << k.get_name() << "\"" << "}";
    return out;
}