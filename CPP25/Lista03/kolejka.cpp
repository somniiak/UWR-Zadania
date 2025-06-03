#include "punkt.hpp"
#include "kolejka.hpp"
#include <algorithm>
#include <stdexcept>
#include <iostream>

kolejka::kolejka() : kolejka(1) {}
kolejka::kolejka(int s) : pojemnosc(s), tab(new punkt[s]) {}
kolejka::kolejka(std::initializer_list<punkt> lista) :
    pojemnosc(lista.size()), ile(lista.size()) {
        if (lista.size() < 1)
            throw std::underflow_error("Minimalna pojemność kolejki to 1!");
        tab = new punkt[lista.size()];
        std::copy(lista.begin(), lista.end(), tab);
    }
kolejka::kolejka(const kolejka &kol) :
    pojemnosc(kol.pojemnosc), pocz(kol.pocz),
    ile(kol.ile), tab(new punkt[kol.pojemnosc]) {
        std::copy(kol.tab, kol.tab + kol.pojemnosc, tab);
        std::cout << "~~Kopiowanie działa!~~" << std::endl;
    }
kolejka::kolejka(kolejka&& kol) : kolejka(kol.pojemnosc) {
        std::swap(kol.tab, tab);
        std::swap(kol.ile, ile);
        std::swap(kol.pocz, pocz);
        std::cout << "~~Przenoszenie działa!~~" << std::endl;
    }
kolejka& kolejka::operator=(const kolejka& kol) {
    if (this != &kol) {
        delete[] tab;
        pojemnosc = kol.pojemnosc;
        pocz = kol.pocz;
        ile = kol.ile;
        tab = new punkt[pojemnosc];
        std::copy(kol.tab, kol.tab + kol.pojemnosc, tab);
    }
    return *this;
}
kolejka& kolejka::operator=(kolejka&& kol) {
    if (this != &kol) {
        std::swap(kol.tab, tab);
        std::swap(kol.ile, ile);
        std::swap(kol.pocz, pocz);
    }
    return *this;
}
kolejka::~kolejka() {
    delete[] tab;
    std::cout << "~~Destruktor działa!~~" << std::endl;
}
void kolejka::wstaw(punkt pun) {
    if (ile == pojemnosc)
        throw std::overflow_error("Kolejka pełna!");
    tab[(pocz + ile) % pojemnosc] = pun;
    ile++;
}
punkt kolejka::usun() {
    if (ile == 0)
        throw std::underflow_error("Kolejka pusta!");
    punkt tmp = tab[pocz];
    pocz = (pocz + 1) % pojemnosc;
    ile--;
    return tmp;
}
punkt kolejka::zprzodu() {
    if (ile == 0)
        throw std::underflow_error("Kolejka pusta!");
    return tab[pocz];
}
int kolejka::dlugosc() { return ile; }