#ifndef WYJATEK_WYMIERNY_HPP
#define WYJATEK_WYMIERNY_HPP

#include <string>
#include <stdexcept>

namespace obliczenia
{
    class wyjatek_wymierny : public std::logic_error
    {
        public:
            explicit wyjatek_wymierny(const std::string& msg)
                : std::logic_error(msg) {}
    };

    class dzielenie_przez_zero : public wyjatek_wymierny
    {
        public:
            dzielenie_przez_zero() : wyjatek_wymierny("Próba dzielenia przez zero!") {}
    };

    class przekroczenie_zakresu : public wyjatek_wymierny
    {
        public:
            przekroczenie_zakresu() : wyjatek_wymierny("Wynik operacji przekracza zakres int!") {}
    };
}

#endif