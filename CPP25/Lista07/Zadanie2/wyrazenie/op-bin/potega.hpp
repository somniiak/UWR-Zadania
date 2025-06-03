#ifndef POTEGA_H
#define POTEGA_H

#include "operator2.hpp"

#include <climits>
#include <stdexcept>

namespace obliczenia
{
    class potega : public operator2
    {
        public:
            potega(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
