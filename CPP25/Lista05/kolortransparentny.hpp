#ifndef KOLORTRANS_H
#define KOLORTRANS_H

#include "kolor.hpp"

class kolortransparentny : public virtual kolor
{
    private:
        ushort alfa;

    public:
        kolortransparentny();
        kolortransparentny(ushort red, ushort green, ushort blue, ushort value);
        ushort get_alpha() const;
        void set_alpha(ushort value);
        friend std::ostream& operator<<(std::ostream &out, const kolortransparentny &k);
};

#endif