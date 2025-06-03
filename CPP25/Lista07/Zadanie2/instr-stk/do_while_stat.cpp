#include "do_while_stat.hpp"

namespace obliczenia
{
    do_while_stat::do_while_stat(wyrazenie* w, instrukcja* i) : w(w), i(i) {
        if (!w || !i)
            throw std::invalid_argument("Argumenty instrukcji \"when\" nie mogą być puste!");
    }

    do_while_stat::~do_while_stat() {
        delete w;
        delete i;
    }

    void do_while_stat::wykonaj() const {
        i->wykonaj();
        while (w->oblicz())
            i->wykonaj();
    }

    std::string do_while_stat::zapis(int wciecie) const {
        std::ostringstream out;
        out << std::string(wciecie, ' ') + "do";

        if(dynamic_cast<blok*>(i))
            out << "\n" + std::string(wciecie, ' ') + "{\n" + i->zapis(wciecie + 4) + std::string(wciecie, ' ') + "}\n";
        else
            out << " " + i->zapis() + "\n";

        out << std::string(wciecie, ' ') + "while (" + w->zapis() + ");";

        return out.str();
    }
}
