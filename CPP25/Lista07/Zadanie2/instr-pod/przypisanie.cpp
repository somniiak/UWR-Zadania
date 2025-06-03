#include "przypisanie.hpp"

namespace obliczenia
{
    przypisanie::przypisanie(zmienna* zm, wyrazenie* wr) : z(zm), w(wr) {
        if (!z || !w)
            throw std::invalid_argument("Zmienne nie mogą być puste!");
    }

    przypisanie::~przypisanie() {
        delete z;
        delete w;
    }

    void przypisanie::wykonaj() const {
        zmienna::ustaw(z->zapis(), w->oblicz());
    }

    std::string przypisanie::zapis(int wciecie) const {
        return std::string(wciecie, ' ') + z->zapis() + " = " + w->zapis() + ";";
    }
}
