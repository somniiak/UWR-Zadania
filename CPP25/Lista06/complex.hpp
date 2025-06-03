#ifndef COMPLEX_H
#define COMPLEX_H

#include <iostream>

namespace math
{
    class complex
    {
        private:
            double r, i;

        public:
            complex(double a = 0, double b = 0) : r(a), i(b) { }

        public:
            double re() const;
            double im() const;
            void re(double r);
            void im(double i);
            complex conjugated() const;
    };

    complex operator+(const complex &x, const complex &y);
    complex operator-(const complex &x, const complex &y);
    complex operator*(const complex &x, const complex &y);
    complex operator/(const complex &x, const complex &y);
    std::ostream& operator<<(std::ostream &os, const complex &c);
    std::istream& operator>>(std::istream &is, complex &c);
}

#endif