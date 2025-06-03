#include "deklaracja.hpp"

namespace obliczenia
{
    deklaracja::deklaracja(std::string name) : z(new zmienna(name)) {}

    deklaracja::~deklaracja() {
        delete z;
    }

    void deklaracja::wykonaj() const {
        zmienna::dodaj(z->zapis(), 0);
    }

    std::string deklaracja::zapis(int wciecie) const {
        return std::string(wciecie, ' ') + "var " + z->zapis() + ";";
    }

    zmienna* deklaracja::pobierz_zmienna() const {
        return z;
    }
}
