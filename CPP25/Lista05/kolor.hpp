#ifndef KOLOR_H
#define KOLOR_H

#include <ostream>
typedef unsigned short ushort;

class kolor
{
    protected:
        ushort r, g, b;

    public:
        kolor();
        kolor(ushort red, ushort green, ushort blue);
        ushort get_r() const;
        ushort get_g() const;
        ushort get_b() const;
        void set_r(ushort red);
        void set_g(ushort green);
        void set_b(ushort blue);
        void darken(float value);
        void lighten(float value);
        static kolor mix(const kolor& k1, const kolor& k2);
        friend std::ostream& operator<<(std::ostream &out, const kolor &k);
};

#endif