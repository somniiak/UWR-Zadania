#ifndef WEJSCIE_HPP
#define WEJSCIE_HPP

#include <fstream>
#include <string>
#include <stdexcept>

class wejscie
{
    private:
        std::ifstream inputFile;
        int encKey = 0;

    public:
        wejscie(const std::string& filename);
        ~wejscie();
        std::string czytaj();
        void ustawKlucz(int k);
};

#endif