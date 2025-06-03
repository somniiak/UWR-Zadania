#ifndef ROZNE_H
#define ROZNE_H

#include "operator2.hpp"

namespace obliczenia
{
    class rozne : public operator2
    {
        public:
            rozne(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
