#include "polynominal.hpp"

namespace calc
{
    int polynominal::get_st() { return n; }

    polynominal::polynominal(int st = 0, complex wsp = complex(1, 0)) : n(st) {
        if (st < 0)
            throw std::invalid_argument("Stopień nie może być ujemny");
        if (st != 0 && wsp.re() == 0 && wsp.im() == 0)
            throw std::invalid_argument("Współczynnik najwyższej potęgi nie może być równy zero!");
        a = new complex[n + 1];
        std::fill(a, a + st + 1, complex(0, 0));
        a[st] = wsp;
    }

    polynominal::polynominal(int st, const complex wsp[]) : n(st) {
        if (st < 0)
            throw std::invalid_argument("Stopień nie może być ujemny");
        if (st != 0 && wsp[st].re() == 0 && wsp[st].im() == 0)
            throw std::invalid_argument("Współczynnik najwyższej potęgi nie może być równy zero!");
        a = new complex[n + 1];
        std::copy(wsp, wsp + n + 1, a);
    }

    polynominal::polynominal(std::initializer_list<complex> wsp) :
        n(wsp.size() - 1), a(new complex[wsp.size()]) {
        if ((wsp.end() - 1)->re() == 0 && (wsp.end() - 1)->im() == 0)
            throw std::invalid_argument("Współczynnik najwyższej potęgi nie może być równy zero!");
        std::copy(wsp.begin(), wsp.end(), a);
    }

    polynominal::polynominal (const polynominal &p) : n(p.n), a(new complex[p.n + 1]) {
        std::copy(p.a, p.a + p.n + 1, a);
    }

    polynominal::polynominal (polynominal &&p) : polynominal() {
        std::swap(n, p.n);
        std::swap(a, p.a);
    }

    polynominal::~polynominal() {
        n = 0; delete[] a;
    }

    polynominal& polynominal::operator=(const polynominal &p) {
        if (this != &p) {
            this->~polynominal();
            n = p.n;
            a = new complex[n + 1];
            std::copy(p.a, p.a + n + 1, a);
        }
        return *this;
    }

    polynominal& polynominal::operator=(polynominal &&p) {
        if (this != &p) {
            std::swap(n, p.n);
            std::swap(a, p.a);
        }
        return *this;
    }

    complex polynominal::operator()(complex x) const {
        complex wynik = a[n];
        for (int i = n - 1; i >= 0; i--)
            wynik = wynik * x + a[i];
        return wynik;
    }

    complex polynominal::operator[](int i) const {
        if (i < 0 || i > n)
            throw std::out_of_range("Indeks poza zakresem!");
        return a[i];
    }

    complex& polynominal::operator[](int i) {
        if (i < 0 || i > n)
            throw std::out_of_range("Indeks poza zakresem!");
        if (i == n && a[i].re() == 0 && a[i].im() == 0)
            throw std::out_of_range("Współczynnik najwyższej potęgi nie może być równy zero.");
        return a[i];
    }

    std::ostream& operator<<(std::ostream &out, const polynominal &p) {
        for (int i = 0 ; i <= p.n ; i++ ) {
            if (p.a[i].re() == 0 && p.a[i].im() == 0)
                continue;
            else if (i == p.n)
                out << "(" << p.a[i] << ")" << "z^" << i;
            else
                out << "(" << p.a[i] << ")" << "z^" << i << " + ";
        }
        return out;
    }


    polynominal operator+(const polynominal &u, const polynominal &v) {
        int max_n = std::max(u.n, v.n);
        polynominal wynik(max_n);

        for (int i = 0; i <= max_n; i++) {
            complex au = (i <= u.n) ? u.a[i] : complex(0, 0);
            complex av = (i <= v.n) ? v.a[i] : complex(0, 0);
            wynik.a[i] = au + av;
        }
        return wynik;
    }

    polynominal operator-(const polynominal &u, const polynominal &v) {
        int max_n = std::max(u.n, v.n);
        polynominal wynik(max_n);

        for (int i = 0; i <= max_n; i++) {
            complex au = (i <= u.n) ? u.a[i] : complex(0, 0);
            complex av = (i <= v.n) ? v.a[i] : complex(0, 0);
            wynik.a[i] = au - av;
        }
        return wynik;
    }

    polynominal operator*(const polynominal &u, const polynominal &v) {
        polynominal wynik(u.n + v.n);
        //wynik[u.n + v.n] = 0; // Domyślnie jest 1 a skoro operator [] nie pozwala na zero to trzeba 1 odjąć
        for (int i = 0; i <= u.n; i++) {
            for (int j = 0; j <= v.n; j++) {
                wynik[i + j] = wynik[i + j] + u.a[i] * v.a[j];
            }
        }
        wynik[u.n + v.n].re(wynik[u.n + v.n].re() - 1);
        return wynik;
    }

    polynominal operator*(complex c, const polynominal &p) {
        polynominal wynik(p.n);
        for (int i = 0; i <= p.n; i++)
            wynik.a[i] = p.a[i] * c;
        return wynik;
    }

    polynominal operator*(const polynominal &p, complex c) {
        polynominal wynik(p.n);
        for (int i = 0; i <= p.n; i++)
            wynik.a[i] = p.a[i] * c;
        return wynik;
    }
}