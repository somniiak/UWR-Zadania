#ifndef MNOZENIE_H
#define MNOZENIE_H

#include "operator2.hpp"

namespace obliczenia
{
    class mnozenie : public operator2
    {
        public:
            mnozenie(wyrazenie* a, wyrazenie *b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
