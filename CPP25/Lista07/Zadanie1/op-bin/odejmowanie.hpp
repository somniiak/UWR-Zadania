#ifndef ODEJMOWANIE_H
#define ODEJMOWANIE_H

#include "operator2.hpp"

namespace obliczenia
{
    class odejmowanie : public operator2
    {
        public:
            odejmowanie(wyrazenie* a, wyrazenie *b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
