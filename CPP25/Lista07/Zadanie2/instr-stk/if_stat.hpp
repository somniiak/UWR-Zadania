#ifndef IF_STAT_H
#define IF_STAT_H

#include "instrukcja.hpp"

namespace obliczenia
{
    class if_stat : public instrukcja
    {
        private:
            wyrazenie* warunek;
            instrukcja* then_stat;

        public:
            if_stat(wyrazenie* warunek, instrukcja* then_stat);
            ~if_stat();
            void wykonaj() const override;
            std::string zapis(int wciecie = 0) const override;
    }; 
}

#endif
