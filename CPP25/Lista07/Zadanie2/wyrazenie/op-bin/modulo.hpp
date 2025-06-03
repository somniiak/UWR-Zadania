#ifndef MODULO_H
#define MODULO_H

#include "operator2.hpp"

namespace obliczenia
{
    class modulo : public operator2
    {
        public:
            modulo(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override; 
    };
}

#endif
