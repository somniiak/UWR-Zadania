#ifndef KOLORTRANSNAZ_H
#define KOLORTRANSNAZ_H

#include "kolortransparentny.hpp"
#include "kolornazwany.hpp"

class kolortransnaz : public kolortransparentny, public kolornazwany
{
    public:
        kolortransnaz(ushort r, ushort g, ushort b, ushort a, std::string n);
        friend std::ostream& operator<<(std::ostream &out, const kolortransnaz &k);
};

#endif