#ifndef WYRAZENIE_H
#define WYRAZENIE_H

#include <string>

namespace obliczenia
{
    class wyrazenie
    {
        public:
            wyrazenie() = default;
            virtual ~wyrazenie() = default;

            wyrazenie(const wyrazenie&) = delete;
            wyrazenie& operator=(const wyrazenie&) = delete;
            wyrazenie(wyrazenie&&) = delete;
            wyrazenie& operator=(wyrazenie&&) = delete;

            virtual int oblicz() const = 0;
            virtual std::string zapis() const = 0;
            virtual int priorytet() const = 0;
            virtual bool lewostronne() const = 0;
    };
}

#endif
