#ifndef MNIEJSZE_H
#define MNIEJSZE_H

#include "operator2.hpp"

namespace obliczenia
{
    class mniejsze : public operator2
    {
        public:
            mniejsze(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
