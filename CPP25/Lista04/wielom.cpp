#include <initializer_list>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <string>
#include "wielom.hpp"

int wielom::get_st() { return n; }

wielom::wielom(int st = 0, double wsp = 1.0) : n(st) {
    if (st < 0)
        throw std::invalid_argument("Stopień nie może być ujemny");
    if (st != 0 && wsp == 0.0)
        throw std::invalid_argument("Współczynnik najwyższej potęgi nie może być równy zero!");
    a = new double[n + 1];
    std::fill(a, a + st + 1, 0.0);
    a[st] = wsp;
}

wielom::wielom (int st, const double wsp[]) : n(st) {
    if (st < 0)
        throw std::invalid_argument("Stopień nie może być ujemny");
    if (st != 0 && wsp[st] == 0.0)
        throw std::invalid_argument("Współczynnik najwyższej potęgi nie może być równy zero!");
    a = new double[n + 1];
    std::copy(wsp, wsp + n + 1, a);
}

wielom::wielom(std::initializer_list<double> wsp) :
    n(wsp.size() - 1), a(new double[wsp.size()]) {
    if (*(wsp.end() - 1) == 0.0)
        throw std::invalid_argument("Współczynnik najwyższej potęgi nie może być równy zero!");
    std::copy(wsp.begin(), wsp.end(), a);
}

wielom::wielom (const wielom &w) : n(w.n), a(new double[w.n + 1]) {
    std::copy(w.a, w.a + w.n + 1, a);
}

wielom::wielom (wielom &&w) : wielom() {
    std::swap(n, w.n);
    std::swap(a, w.a);
}

wielom& wielom::operator=(const wielom &w) {
    if (this != &w) {
        this->~wielom(); // "this" to wskaźnik?
        n = w.n;
        a = new double[n + 1];
        std::copy(w.a, w.a + n + 1, a);
    }
    return *this;
}

wielom& wielom::operator=(wielom &&w) {
    if (this != &w) {
        std::swap(n, w.n);
        std::swap(a, w.a);
    }
    return *this;
}

wielom::~wielom() {
    n = 0; delete[] a;
}

// Fajny PDF
// https://home.csulb.edu/~pnguyen/cecs282/lecnotes/Operator%20Overloading.pdf
std::ostream& operator<<(std::ostream &out, const wielom &w) {
    for (int i = 0 ; i <= w.n ; i++ ) {
        if (i == 0 && w.a[i] != 0)
            out << w.a[i] << " + ";
        else if (i == w.n)
            out << w.a[i] << "x^" << i;
        else if (w.a[i] != 0)
            out <<  w.a[i] << "x^" << i << " + ";
    }
    return out;
}

std::istream& operator>>(std::istream &in, wielom &w) {
    for (int i = 0; i <= w.n; i++) {
        std::cout << "Współczynnik x^" << i << ": ";

        std::string wejscie;
        in >> wejscie;

        try {
            w.a[i] = std::stod(wejscie);
            if(i == w.n && w.a[i] == 0) {
                std::cerr << "Współczynnik najwyższej potęgi nie może być równy zero. ";
                std::cerr << "Spróbuj ponownie." << std::endl;
                i--;
            }
        }
        catch (const std::invalid_argument&) {
            // https://overflow.hostux.net/questions/5131647/why-would-we-call-cin-clear-and-cin-ignore-after-reading-input
            std::cerr << "Podano niepoprawną wartością! Spróbuj ponownie." << std::endl;
            in.clear();
            in.ignore(10000,'\n');      
            i--;
        }
    }
    return in;
}

wielom operator+(const wielom &u, const wielom &v) {
    int max_n = std::max(u.n, v.n);
    wielom wynik(max_n);

    for (int i = 0; i <= max_n; i++) {
        double au = (i <= u.n) ? u.a[i] : 0.0;
        double av = (i <= v.n) ? v.a[i] : 0.0;
        wynik.a[i] = au + av;
    }
    return wynik;
}

wielom operator-(const wielom &u, const wielom &v) {
    int max_n = std::max(u.n, v.n);
    wielom wynik(max_n);

    for (int i = 0; i <= max_n; i++) {
        double au = (i <= u.n) ? u.a[i] : 0.0;
        double av = (i <= v.n) ? v.a[i] : 0.0;
        wynik.a[i] = au - av;
    }
    return wynik;
}

wielom operator*(const wielom &u, const wielom &v) {
    wielom wynik(u.n + v.n);
    //wynik[u.n + v.n] = 0; // Domyślnie jest 1 a skoro operator [] nie pozwala na zero to trzeba 1 odjąć
    for (int i = 0; i <= u.n; i++) {
        for (int j = 0; j <= v.n; j++) {
            wynik[i + j] += u.a[i] * v.a[j];
        }
    }
    wynik[u.n + v.n] -= 1;
    return wynik;
}

wielom operator*(double c, const wielom &w) {
    wielom wynik(w.n);
    for (int i = 0; i <= w.n; i++)
        wynik.a[i] = w.a[i] * c;
    return wynik;
}

wielom operator*(const wielom &w, double c) {
    wielom wynik(w.n);
    for (int i = 0; i <= w.n; i++)
        wynik.a[i] = w.a[i] * c;
    return wynik;
}

wielom& wielom::operator+=(const wielom &v) {
    if (n < v.n) {
        double* new_a = new double[v.n + 1];
        for (int i = 0; i <= v.n; i++)
            new_a[i] = (i <= n) ? a[i] : 0.0;
        n = v.n;
        delete[] a;
        a = new_a;
    }
    for (int i = 0; i <= n; i++)
        a[i] += (i <= v.n) ? v.a[i] : 0.0;
    return *this;
}

wielom& wielom::operator-=(const wielom &v) {
    if (n < v.n) {
        double* new_a = new double[v.n + 1];
        for (int i = 0; i <= v.n; i++)
            new_a[i] = (i <= n) ? a[i] : 0.0;
        n = v.n;
        delete[] a;
        a = new_a;
    }
    for (int i = 0; i <= n; i++)
        a[i] -= (i <= v.n) ? v.a[i] : 0.0;
    return *this;
}

wielom& wielom::operator*=(const wielom &v) {
    double* new_a = new double[n + v.n + 1];
    for (int i = 0; i <= n + v.n; i++)
        new_a[i] = 0.0;
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= v.n; j++) {
            new_a[i + j] += a[i] * v.a[j];
        }
    }
    delete[] a;
    a = new_a;
    n += v.n;
    return *this;
}

wielom& wielom::operator*=(double c) {
    for (int i = 0; i <= n; i++)
        a[i] *= c;
    return *this;
}

double wielom::operator()(double x) const {
    double wynik = a[n];
    for (int i = n - 1; i >= 0; i--)
        wynik = wynik * x + a[i];
    return wynik;
}

double wielom::operator[](int i) const {
    if (i < 0 || i > n)
        throw std::out_of_range("Indeks poza zakresem!");
    return a[i];
}

double& wielom::operator[](int i) {
    if (i < 0 || i > n)
        throw std::out_of_range("Indeks poza zakresem!");
    if (i == n && a[i] == 0)
        throw std::out_of_range("Współczynnik najwyższej potęgi nie może być równy zero.");
    return a[i];
}