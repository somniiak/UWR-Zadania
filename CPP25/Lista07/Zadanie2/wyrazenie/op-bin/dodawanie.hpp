#ifndef DODAWANIE_H
#define DODAWANIE_H

#include "operator2.hpp"

namespace obliczenia
{
    class dodawanie : public operator2
    {
        public:
            dodawanie(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
