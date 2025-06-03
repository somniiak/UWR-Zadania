#ifndef WIEKSZE_H
#define WIEKSZE_H

#include "operator2.hpp"

namespace obliczenia
{
    class wieksze : public operator2
    {
        public:
            wieksze(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
