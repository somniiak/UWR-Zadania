#ifndef ROWNE_H
#define ROWNE_H

#include "operator2.hpp"

namespace obliczenia
{
    class rowne : public operator2
    {
        public:
            rowne(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
