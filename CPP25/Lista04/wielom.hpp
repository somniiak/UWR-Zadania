#ifndef WIELOM_HPP
#define WIELOM_HPP

#include <initializer_list>

class wielom
{
    private:
        int n; // Stopień wielomianu
        double* a; // Współczynniki wielomianu;

    public:
        int get_st();
        wielom(int st, double wsp); // konstruktor jednomianu
        wielom(int st, const double wsp[]); // konstruktor wielomianu
        wielom(std::initializer_list<double> wsp); // lista współczynników
        wielom(const wielom &w); // konstruktor kopiujący
        wielom(wielom &&w); // konstruktor przenoszący
        wielom& operator=(const wielom &w); // przypisanie kopiujące
        wielom& operator=(wielom &&w); // przypisanie przenoszące
        ~wielom(); // destruktor
        friend std::ostream& operator<<(std::ostream &out, const wielom &w);
        friend std::istream& operator>>(std::istream &in, wielom &w);
        friend wielom operator+(const wielom &u, const wielom &v);
        friend wielom operator-(const wielom &u, const wielom &v);
        friend wielom operator*(const wielom &u, const wielom &v);
        friend wielom operator*(double c, const wielom &w);
        friend wielom operator*(const wielom &w, double c);
        wielom& operator+=(const wielom &v);
        wielom& operator-=(const wielom &v);
        wielom& operator*=(const wielom &v);
        wielom& operator*=(double c);
        double operator()(double x) const; // wartość wielomianu dla x
        double operator[](int i) const; // do odczytu współczynnika
        double& operator[](int i); // do zapisu współczynnika
};

#endif