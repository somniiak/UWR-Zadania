#ifndef MNIEJSZE_ROWNE_H
#define MNIEJSZE_ROWNE_H

#include "operator2.hpp"

namespace obliczenia
{
    class mniejsze_rowne : public operator2
    {
        public:
            mniejsze_rowne(wyrazenie* a, wyrazenie* b);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
