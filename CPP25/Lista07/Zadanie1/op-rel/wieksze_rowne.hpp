#ifndef WIEKSZE_ROWNE_H
#define WIEKSZE_ROWNE_H

#include "operator2.hpp"

namespace obliczenia
{
    class wieksze_rowne : public operator2
    {
        public:
            wieksze_rowne(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
