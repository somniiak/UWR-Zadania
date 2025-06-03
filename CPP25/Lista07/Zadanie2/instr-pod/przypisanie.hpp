#ifndef PRZYPISANIE_H
#define PRZYPISANIE_H

#include "instrukcja.hpp"

namespace obliczenia
{
    class przypisanie : public instrukcja
    {
        private:
            zmienna* z;
            wyrazenie* w;

        public:
            przypisanie(zmienna* zm, wyrazenie* wr);
            ~przypisanie();
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
    };
}

#endif
