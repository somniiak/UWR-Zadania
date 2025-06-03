#ifndef LICZBA_H
#define LICZBA_H

#include "wyrazenie.hpp"

namespace obliczenia
{
    class liczba : public wyrazenie
    {
        private:
            int wartosc;

        public:
            liczba(int w);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };
}

#endif
