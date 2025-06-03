#include "stala.hpp"

namespace obliczenia
{
    stala::stala(std::string n, int w) : nazwa(n), wartosc(w) {}

    int stala::oblicz() const {
        return wartosc;
    }
    std::string stala::zapis() const {
        return nazwa;
    }
    int stala::priorytet() const {
        return 100;
    }
    bool stala::lewostronne() const {
        return true;
    }
}
