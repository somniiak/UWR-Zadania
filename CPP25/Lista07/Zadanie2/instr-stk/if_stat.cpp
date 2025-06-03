#include "if_stat.hpp"
#include "blok.hpp"

namespace obliczenia
{
    if_stat::if_stat(wyrazenie* warunek, instrukcja* then_stat) :
    warunek(warunek), then_stat(then_stat) {
        if (!warunek || !then_stat)
            throw std::invalid_argument("Argumenty instrukcji \"if\" nie mogą być puste!");
    }

    if_stat::~if_stat() {
        delete warunek;
        delete then_stat;
    }

    void if_stat::wykonaj() const {
        if (warunek->oblicz())
            then_stat->wykonaj();
    }

    std::string if_stat::zapis(int wciecie) const {
        std::ostringstream out;
        out << std::string(wciecie, ' ') + "if (" + warunek->zapis() + ")";

        if(dynamic_cast<blok*>(then_stat))
            out << "\n" + std::string(wciecie, ' ') + "{\n" + then_stat->zapis(wciecie + 4) + std::string(wciecie, ' ') + "}";
        else
            out << " " + then_stat->zapis();

        return out.str();
    } 
}
