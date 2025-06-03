#ifndef STALA_H
#define STALA_H

#include "wyrazenie.hpp"

namespace obliczenia
{
    class stala : public wyrazenie
    {
        private:
            std::string nazwa;
            int wartosc;

        public:
            stala(std::string n, int w);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
    };

    class zero : public stala
    {
        public:
            zero() : stala("0", 0) {};
    };

    class jeden : public stala
    {
        public:
            jeden() : stala("1", 1) {};
    };
}

#endif
