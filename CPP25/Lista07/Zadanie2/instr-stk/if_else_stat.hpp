#ifndef IF_ELSE_STAT_H
#define IF_ELSE_STAT_H

#include "instrukcja.hpp"

namespace obliczenia
{
    class if_else_stat : public instrukcja
    {
        private:
            wyrazenie* warunek;
            instrukcja* then_stat;
            instrukcja* else_stat;

        public:
            if_else_stat(wyrazenie* warunek, instrukcja* then_stat, instrukcja* else_stat);
            ~if_else_stat();
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
    };
}

#endif
