#include "zmienna.hpp"

namespace obliczenia
{
    std::vector<std::pair<std::string, int>> zmienna::zmienne;

    zmienna::zmienna(std::string n) : nazwa(n) {};

    int zmienna::oblicz() const {
        int idx = znajdz(nazwa);
        if (idx == -1)
            throw std::runtime_error("Nieznana zmienna: " + nazwa);
        return zmienne[idx].second;
    }
    std::string zmienna::zapis() const {
        return nazwa;
    }
    int zmienna::priorytet() const {
        return 100;
    }
    bool zmienna::lewostronne() const {
        return true;
    }
    int zmienna::znajdz(std::string n) {
        for (unsigned long int i = 0; i < zmienne.size(); i++) {
            if(zmienne[i].first == n)
                return static_cast<int>(i);
        }
        return -1;
    }
    void zmienna::dodaj(std::string n, int v) {
        if (znajdz(n) == -1)
            zmienne.push_back(std::pair(n, v));
        else
            throw std::runtime_error("Zmienna już istnieje: " + n);
    }
    void zmienna::ustaw(std::string n, int v) {
        int idx = znajdz(n);
        if (idx != -1)
            zmienne[idx].second = v;
        else
            throw std::runtime_error("Nie można ustawić wartości nieistniejacej zmiennej: " + n);
    }
    void zmienna::usun(std::string n) {
        int idx = znajdz(n);
        if (idx != -1)
            zmienne.erase(zmienne.begin() + idx);
        else
            throw std::runtime_error("Nie można usunąć nieistniejacej zmiennej: " + n);
    }
}
