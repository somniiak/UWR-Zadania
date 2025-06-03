#ifndef BLOK_H
#define BLOK_H

#include "instrukcja.hpp"

namespace obliczenia
{
    class blok : public instrukcja
    {
        private:
            std::vector<instrukcja*> instrukcje;

        public:
            blok(std::initializer_list<instrukcja*> lista);
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
    };
}

#endif
