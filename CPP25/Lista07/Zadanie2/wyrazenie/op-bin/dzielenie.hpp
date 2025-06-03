#ifndef DZIELENIE_H
#define DZIELENIE_H

#include "operator2.hpp"

namespace obliczenia
{
    class dzielenie : public operator2
    {
        public:
            dzielenie(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
