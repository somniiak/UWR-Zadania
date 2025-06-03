#ifndef CZYTANIE_H
#define CZYTANIE_H

#include "instrukcja.hpp"

namespace obliczenia
{
    class czytanie : public instrukcja
    {
        private:
            zmienna* z;
            std::string n;

        public:
            czytanie(zmienna* z);
            ~czytanie();
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
    };
}

#endif
