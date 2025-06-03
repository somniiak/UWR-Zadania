#ifndef PIKSELKOL_H
#define PIKSELKOL_H

#include "piksel.hpp"
#include "kolor.hpp"

class pikselkolorowy : public piksel, private kolor
{
    public:
        pikselkolorowy();
        pikselkolorowy(int nx, int ny, ushort r, ushort g, ushort b);
        void shift_by(int dx, int dy);
        friend std::ostream& operator<<(std::ostream &out, const pikselkolorowy &p);
};

#endif