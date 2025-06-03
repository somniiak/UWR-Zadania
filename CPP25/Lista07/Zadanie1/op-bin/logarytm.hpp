#ifndef LOGARYTM_H
#define LOGARYTM_H

#include "operator2.hpp"

#include <stdexcept>

namespace obliczenia
{
    class logarytm : public operator2
    {
        public:
            logarytm(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
