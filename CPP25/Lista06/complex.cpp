#include "complex.hpp"
#include <stdexcept>
#include <string>

namespace math
{
    double complex::re() const { return r ;}
    double complex::im() const { return i; }
    void complex::re(double r) { this->r = r; }
    void complex::im(double i) { this->i = i; }
    complex complex::conjugated() const { return complex(r, -i); }
    complex operator+(const complex &x, const complex &y) { return complex(x.re() + y.re(), x.im() + y.im()); }
    complex operator-(const complex &x, const complex &y) { return complex(x.re() - y.re(), x.im() - y.im()); }

    complex operator*(const complex &x, const complex &y) {
        return complex(
            x.re() * y.re() - x.im() * y.im(),
            x.re() * y.im() + x.im() * y.re()
        );
    }

    complex operator/(const complex &x, const complex &y) {
        if (y.re() == 0 && y.im() == 0)
            throw std::out_of_range("Mianownik nie może być równy zero!");
        return complex(
            (x.re() * y.re() + x.im() * y.im()) / (y.re() * y.re() + y.im() * y.im()),
            (x.im() * y.re() - x.re() * y.im()) / (y.re() * y.re() + y.im() * y.im())
        );
    }

    std::ostream& operator<<(std::ostream &os, const complex &c) {
        if (c.im() < 0) { os << c.re() << c.im() << "i"; }
        else { os<< c.re() << "+" << c.im() << "i"; }
        return os;
    }
    
    std::istream& operator>>(std::istream &is, complex &c) {
        std::string input;
        double real, imag;

        while(true) {
            std::cout << "Re: "; is >> input;
            try {
                real = std::stod(input);
                c.re(real);
                break;
            }
            catch (const std::invalid_argument& e) {
                std::cerr << "Podano niepoprawną wartością! Spróbuj ponownie." << std::endl;
                is.clear();
                is.ignore(10000,'\n');
            }
        }

        while(true) {
            std::cout << "Im: "; is >> input;
            try {
                imag = std::stod(input);
                c.im(imag);
                break;
            }
            catch (const std::invalid_argument& e) {
                std::cerr << "Podano niepoprawną wartością! Spróbuj ponownie." << std::endl;
                is.clear();
                is.ignore(10000,'\n');
            }
        }

        return is;
    }
}