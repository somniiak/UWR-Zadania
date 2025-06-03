#ifndef EXCEPTIONS_HPP
#define EXCEPTIONS_HPP

#include <string>
#include <stdexcept>

class wyjatek_samotnika : public std::logic_error
{
    public:
        explicit wyjatek_samotnika(const std::string& msg)
            : std::logic_error(msg) {}
};

class niepoprawny_format : public wyjatek_samotnika
{
    public:
        niepoprawny_format() : wyjatek_samotnika("Niepoprawny format!") {}
};

class niepoprawna_kolumna : public wyjatek_samotnika
{
    public:
        niepoprawna_kolumna() : wyjatek_samotnika("Niepoprawna kolumna!") {}
};

class niepoprawny_wiersz : public wyjatek_samotnika
{
    public:
        niepoprawny_wiersz() : wyjatek_samotnika("Niepoprawny wiersz!") {}
};

class niepoprawny_kierunek : public wyjatek_samotnika
{
    public:
        niepoprawny_kierunek() : wyjatek_samotnika("Niepoprawny kierunek!") {}
};

class niedozwolony_ruch : public wyjatek_samotnika
{
    public:
        niedozwolony_ruch() : wyjatek_samotnika("Niedozwolony ruch!") {}
};

#endif