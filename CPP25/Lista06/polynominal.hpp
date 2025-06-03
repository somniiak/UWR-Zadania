#ifndef POLYNOMINAL_H
#define POLYNOMINAL_H

#include "complex.hpp"

#include <initializer_list>
#include <iostream>

using math::complex;

namespace calc
{
    class polynominal
    {
        private:
            int n; // stopień wielomianu
            complex *a; // współczynniki wielomianu;

        public:
            int get_st();
            polynominal(int st, complex wsp); // konstruktor jednomianu
            polynominal(int st, const complex wsp[]); // konstruktor wielomianu
            polynominal(std::initializer_list<complex> wsp); // lista współczynników
            polynominal(const polynominal &p); // konstruktor kopiujący
            polynominal(polynominal &&p); // konstruktor przenoszący
            ~polynominal(); // destruktor
            polynominal& operator=(const polynominal &p); // przypisanie kopiujące
            polynominal& operator=(polynominal &&p); // przypisanie przenoszące
            complex operator()(complex x) const; // wartość wielomianu dla x
            complex operator[](int i) const; // do odczytu współczynnika
            complex& operator[](int i); // do zapisu współczynnika
            friend std::ostream& operator<<(std::ostream &out, const polynominal &p);
            friend polynominal operator+(const polynominal &u, const polynominal &v);
            friend polynominal operator-(const polynominal &u, const polynominal &v);
            friend polynominal operator*(const polynominal &u, const polynominal &v);
            friend polynominal operator*(complex c, const polynominal &p);
            friend polynominal operator*(const polynominal &p, complex c);
    };
}

#endif