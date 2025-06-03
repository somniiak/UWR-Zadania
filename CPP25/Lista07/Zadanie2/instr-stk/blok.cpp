#include "blok.hpp"
#include "deklaracja.hpp"

namespace obliczenia
{
    blok::blok(std::initializer_list<instrukcja*> lista) {
        for (instrukcja* i : lista) {
            if (!i)
                throw std::invalid_argument("Instrukcja w bloku nie moze być pusta");
            instrukcje.push_back(i);
        }
    }

    void blok::wykonaj() const {
        // Zapisujemy zmienne tutaj bo funkcja jest const
        std::vector<std::string> lokalne_zmienne;

        for (instrukcja* i : instrukcje) {
            // Jeśli jedna z instrukcji to deklaracja trzeba
            // dodać zmienną do wektora zmiennych lokalnych
            deklaracja* t = dynamic_cast<deklaracja*>(i);
            if (t) {
                zmienna* zm = t->pobierz_zmienna();
                lokalne_zmienne.push_back(zm->zapis());
            }
            i->wykonaj();
        }

        // Usuwamy zmienne po wykonaniu
        for (std::string s : lokalne_zmienne) {
            zmienna::usun(s);
        }
    }

    std::string blok::zapis(int wciecie) const {
        std::ostringstream out;
        for (instrukcja* i : instrukcje)
            out << i->zapis(wciecie) << "\n";
        return out.str();
    }
}
