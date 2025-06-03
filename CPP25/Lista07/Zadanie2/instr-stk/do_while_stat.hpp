#ifndef DO_WHILE_STAT_H
#define DO_WHILE_STAT_H

#include "instrukcja.hpp"
#include "blok.hpp"

namespace obliczenia
{
    class do_while_stat : public instrukcja
    {
        private:
        wyrazenie* w;
        instrukcja* i;

        public:
            do_while_stat(wyrazenie* w, instrukcja* i);
            ~do_while_stat();
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
    };
}

#endif
