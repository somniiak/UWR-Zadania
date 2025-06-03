#ifndef INSTRUKCJA_H
#define INSTRUKCJA_H

#include <initializer_list>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

#include "libwyrazenie.hpp"

namespace obliczenia
{
    class instrukcja
    {
        public:
            instrukcja() = default;
            virtual ~instrukcja() = default;

            instrukcja(const instrukcja&) = delete;
            instrukcja& operator=(const instrukcja&) = delete;
            instrukcja(instrukcja&&) = delete;
            instrukcja& operator=(instrukcja&&) = delete;

            virtual void wykonaj() const = 0;
            virtual std::string zapis(int wciecie = 0) const = 0;
    };
}

#endif
