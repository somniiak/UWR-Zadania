#include "pisanie.hpp"

namespace obliczenia
{
    pisanie::pisanie(wyrazenie* w) : w(w) {
        if (!w)
            throw std::invalid_argument("Wyrażenie nie może być puste!");
    }

    pisanie::~pisanie() {
        delete w;
    }

    void pisanie::wykonaj() const {
        std::cout << w->oblicz() << std::endl;
    }

    std::string pisanie::zapis(int wciecie) const {
        return std::string(wciecie, ' ') + "write " + w->zapis() + ";";
    }
}
