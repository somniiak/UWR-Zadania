#ifndef WYMIERNA_HPP
#define WYMIERNA_HPP

#include <stdexcept>
#include <iostream>
#include <numeric>
#include <climits>
#include <cmath>
#include <string>
#include <map>

namespace obliczenia
{
    class wymierna
    {
        private:
            int licz, mian;

        public:
            wymierna(int l, int m);
            explicit wymierna(int l);
            wymierna();
            void reduce();
            int get_licz() const;
            int get_mian() const;
            friend std::ostream& operator<<(std::ostream &out, const wymierna &v);
            friend wymierna operator+(const wymierna &u, const wymierna &v);
            friend wymierna operator-(const wymierna &u, const wymierna &v);
            friend wymierna operator*(const wymierna &u, const wymierna &v);
            friend wymierna operator/(const wymierna &u, const wymierna &v);
            wymierna& operator+=(const wymierna &v);
            wymierna& operator-=(const wymierna &v);
            wymierna& operator*=(const wymierna &v);
            wymierna& operator/=(const wymierna &v);
            wymierna& operator-();
            wymierna& operator!();
            operator double() const;
            explicit operator int() const;
    };
}

#endif