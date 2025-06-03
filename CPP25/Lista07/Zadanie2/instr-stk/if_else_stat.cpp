#include "if_else_stat.hpp"
#include "blok.hpp"

namespace obliczenia
{
    if_else_stat::if_else_stat(wyrazenie* warunek, instrukcja* then_stat, instrukcja* else_stat) :
    warunek(warunek), then_stat(then_stat), else_stat(else_stat) {
        if(!warunek || ! then_stat || !else_stat)
            throw std::invalid_argument("Argumenty instrukcji \"if-else\" nie mogą być puste!");
    }

    if_else_stat::~if_else_stat() {
        delete warunek;
        delete then_stat;
        delete else_stat;
    }

    void if_else_stat::wykonaj() const {
        if (warunek->oblicz())
            then_stat->wykonaj();
        else
            else_stat->wykonaj();
    }

    std::string if_else_stat::zapis(int wciecie) const {
        std::ostringstream out;
        out << std::string(wciecie, ' ') + "if (" + warunek->zapis() + ") " + then_stat->zapis() + "\n";
        out << std::string(wciecie, ' ') + "else";

        // Sprawdzanie czy else_stat jest blokiem wyrażeń (czy należy do klasy blok),
        // bo w takim wypadku należy dodać nawiasy klamrowe i wcięcia. Jeśli to
        // pojedyńcza instrukcja można ją dodać w tej samej linijce.
        if(dynamic_cast<blok*>(else_stat))
            out << "\n" + std::string(wciecie, ' ') + "{\n" + else_stat->zapis(wciecie + 4) + std::string(wciecie, ' ') + "}";

        else
            out << " " + else_stat->zapis();

        return out.str();
    }
}
