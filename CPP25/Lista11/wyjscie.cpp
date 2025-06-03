#include "wyjscie.hpp"

wyjscie::wyjscie(const std::string& filename) {
    outputFile.open(filename);
    if (!outputFile)
        throw std::ios_base::failure("Nie można otworzyć pliku do zapisu.");
    outputFile.exceptions(std::ofstream::failbit | std::ofstream::badbit);
}

wyjscie::~wyjscie() {
    if (outputFile.is_open())
        outputFile.close();
}

void wyjscie::pisz(const std::string& line) {
    outputFile << szyfr::szyfrujTekst(line, encKey) << '\n';
}

void wyjscie::ustawKlucz(int k) {
    encKey = (k % 26 + 26) % 26;
}
