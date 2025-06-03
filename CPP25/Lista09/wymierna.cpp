#include "wymierna.hpp"
#include "wyjatki.hpp"

namespace obliczenia
{
    wymierna::wymierna(int l, int m) {
        if (m == 0)
            throw dzielenie_przez_zero();

        if (m < 0) {
            if (m == INT_MIN)
                throw przekroczenie_zakresu();
            l = -l;
            m = -m;
        }

        licz = l;
        mian = m;

        reduce();
    }

    wymierna::wymierna(int l) : wymierna(l, 1) {}

    wymierna::wymierna() : wymierna(0, 1) {}

    void wymierna::reduce() {
        int d = std::gcd(licz, mian);
        licz /= d;
        mian /= d;
    }

    int wymierna::get_licz() const { return licz; }

    int wymierna::get_mian() const { return mian; }

    // https://stackoverflow.com/questions/1315595/algorithm-for-detecting-repeating-decimals
    // https://en.wikipedia.org/wiki/Repeating_decimal
    std::ostream& operator<<(std::ostream &out, const wymierna &v) {
        if (v.licz < 0)
            out << "-";
        int num = std::abs(v.licz);
        int den = std::abs(v.mian);

        out << (num / den);
        num %= den;

        // Brak części dziesiętnej
        if (num == 0)
            return out;
        out << ".";

        std::map<int, int> remainder_pos;
        int repetend_pos = -1;
        int current_pos = 0;
        std::string decimal;

        while (num != 0) {
            if(remainder_pos.count(num)) {
                repetend_pos = remainder_pos[num];
                break;
            }

            remainder_pos[num] = current_pos;
            num *= 10;
            decimal += std::to_string(num / den);
            num %= den;

            current_pos++;
        }

        // Część skończona
        if (repetend_pos == -1)
            out << decimal;
        // Część okresowa
        else {
            out << decimal.substr(0, repetend_pos);
            out << "(" << decimal.substr(repetend_pos) << ")";
        }

        return out;
    }


    // https://stackoverflow.com/questions/199333/how-do-i-detect-unsigned-integer-overflow
    wymierna operator+(const wymierna &u, const wymierna &v) {
        // Przekroczenie zakresu w liczniku
        if (
            (v.licz * u.mian > 0 && u.licz * v.mian > INT_MAX - v.licz * u.mian) ||
            (v.licz * u.mian < 0 && u.licz * v.mian < INT_MIN - v.licz * u.mian)
        ) throw przekroczenie_zakresu();

        return wymierna(u.licz * v.mian + v.licz * u.mian, u.mian * v.mian);
    }

    wymierna operator-(const wymierna &u, const wymierna &v) {
        // Przekroczenie zakresu w liczniku
        if (
            (v.licz * u.mian < 0 && u.licz * v.mian > INT_MAX + v.licz * u.mian) ||
            (v.licz * u.mian > 0 && u.licz * v.mian < INT_MIN + v.licz * u.mian)
        ) throw przekroczenie_zakresu();

        return wymierna(u.licz * v.mian - v.licz * u.mian, u.mian * v.mian);
    }

    wymierna operator*(const wymierna &u, const wymierna &v) {
        // Przekroczenie zakresu w liczniku
        if (
            (v.licz != 0 && u.licz > INT_MAX / v.licz) ||
            (v.licz != 0 && u.licz < INT_MIN / v.licz) ||
            (v.licz == -1 && u.licz == INT_MIN) ||
            (u.licz == -1 && v.licz == INT_MIN)
        ) throw przekroczenie_zakresu();
        // Przekroczenie zakresu w mianowniku
        if (
            (v.mian != 0 && u.mian > INT_MAX / v.mian) ||
            (v.mian != 0 && u.mian < INT_MIN / v.mian)
        ) throw przekroczenie_zakresu();

        return wymierna(u.licz * v.licz, u.mian * v.mian);
    }

    wymierna operator/(const wymierna &u, const wymierna &v) {
        return (u * wymierna(v.mian, v.licz));
    }

    wymierna& wymierna::operator+=(const wymierna &v) {
        *this = *this + v; return *this;
    }

    wymierna& wymierna::operator-=(const wymierna &v) {
        *this = *this - v; return *this;
    }

    wymierna& wymierna::operator*=(const wymierna &v) {
        *this = *this * v; return *this;
    }

    wymierna& wymierna::operator/=(const wymierna &v) {
        *this = *this / v; return *this;
    }

    wymierna& wymierna::operator-() {
        if (licz == INT_MIN)
            throw przekroczenie_zakresu();
        licz = -licz; return *this;
    }

    wymierna& wymierna::operator!() {
        *this = wymierna(mian, licz); return *this;
    }

    wymierna::operator double() const {
        return static_cast<double>(licz) / mian;
    }

    wymierna::operator int() const {
        return static_cast<int>(
            std::round(
                static_cast<double>(*this)
            )
        );
    }
}