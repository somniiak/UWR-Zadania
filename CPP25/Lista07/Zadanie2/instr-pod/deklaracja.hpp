#ifndef DEKLARACJA_H
#define DEKLARACJA_H

#include "instrukcja.hpp"

namespace obliczenia
{
    class deklaracja : public instrukcja
    {
        private:
            zmienna* z;

        public:
            deklaracja(std::string name);
            ~deklaracja();
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
            zmienna* pobierz_zmienna() const;
    };
}

#endif
