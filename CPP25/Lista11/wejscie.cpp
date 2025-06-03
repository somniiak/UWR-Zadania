#include "wejscie.hpp"

wejscie::wejscie(const std::string& filename) {
    inputFile.open(filename);
    if (!inputFile)
        throw std::ios_base::failure("Nie można otworzyć pliku do odczytu.");
    inputFile.exceptions(std::ifstream::failbit | std::ifstream::badbit);
}

wejscie::~wejscie() {
    if (inputFile.is_open())
        inputFile.close();
}

std::string wejscie::czytaj() {
    std::string line;
    std::getline(inputFile, line);
    return line;
}

void wejscie::ustawKlucz(int k) {
    encKey = (k % 26 + 26) % 26;
}
