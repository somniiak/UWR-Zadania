#include "liczba.hpp"

namespace obliczenia
{
    liczba::liczba(int w) : wartosc(w) {}

    int liczba::oblicz() const {
        return wartosc;
    }
    std::string liczba::zapis() const {
        return std::to_string(wartosc);
    }
    int liczba::priorytet() const {
        return 100;
    }
    bool liczba::lewostronne() const {
        return true;
    }
}
