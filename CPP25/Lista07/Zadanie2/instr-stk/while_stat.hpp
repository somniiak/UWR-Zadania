#ifndef WHILE_STAT_H
#define WHILE_STAT_H

#include "instrukcja.hpp"

namespace obliczenia
{
    class while_stat : public instrukcja
    {
        private:
            wyrazenie* w;
            instrukcja* i;

        public:
            while_stat(wyrazenie* w, instrukcja* i);
            ~while_stat();
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
    };
}

#endif
