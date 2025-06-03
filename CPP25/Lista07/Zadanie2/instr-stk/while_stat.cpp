#include "while_stat.hpp"
#include "blok.hpp"

namespace obliczenia
{
    while_stat::while_stat(wyrazenie* w, instrukcja* i) : w(w), i(i) {
        if (!w || !i)
            throw std::invalid_argument("Argumenty instrukcji \"when\" nie mogą być puste!");
    }

    while_stat::~while_stat() {
        delete w;
        delete i;
    }

    void while_stat::wykonaj() const {
        while (w->oblicz())
            i->wykonaj();
    }

    std::string while_stat::zapis(int wciecie) const {
        std::ostringstream out;
        out << std::string(wciecie, ' ') + "while (" + w->zapis() + ")";

        if(dynamic_cast<blok*>(i))
            out << "\n" + std::string(wciecie, ' ') + "{\n" + i->zapis(wciecie + 4) + std::string(wciecie, ' ') + "}";
        else
            out << " " + i->zapis();
        
        return out.str();
    }
}
