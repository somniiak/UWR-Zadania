#ifndef MINUS_H
#define MINUS_H

#include "operator1.hpp"

namespace obliczenia
{
    class minus : public operator1
    {
        public:
            minus(wyrazenie* w);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
