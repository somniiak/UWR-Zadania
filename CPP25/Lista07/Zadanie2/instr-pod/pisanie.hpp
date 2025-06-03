#ifndef PISANIE_H
#define PISANIE_H

#include "instrukcja.hpp"

namespace obliczenia
{
    class pisanie : public instrukcja
    {
        private:
            wyrazenie* w;

        public:
            pisanie(wyrazenie* w);
            ~pisanie();
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
    };
}

#endif
