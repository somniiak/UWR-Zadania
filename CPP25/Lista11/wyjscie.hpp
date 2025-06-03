#ifndef WYJSCIE_HPP
#define WYJSCIE_HPP

#include "szyfr.hpp"

#include <fstream>
#include <string>
#include <stdexcept>

class wyjscie
{
    private:
        std::ofstream outputFile;
        int encKey = 0;

    public:
        wyjscie(const std::string& filename);
        ~wyjscie();
        void pisz(const std::string& line);
        void ustawKlucz(int k);
};

#endif