#ifndef ZMIENNA_H
#define ZMIENNA_H

#include "wyrazenie.hpp"

#include <vector>
#include <utility>
#include <stdexcept>

namespace obliczenia
{
    class zmienna : public wyrazenie
    {
        private:
            std::string nazwa;
            static std::vector<std::pair<std::string, int>> zmienne;
            static int znajdz(std::string n);

        public:
            zmienna(std::string n);
            int oblicz() const override;
            std::string zapis() const override;
            int priorytet() const override;
            bool lewostronne() const override;
            static void dodaj(std::string n, int v);
            static void ustaw(std::string n, int v);
            static void usun(std::string n);
    };
}

#endif
