#include "czytanie.hpp"

namespace obliczenia
{
    czytanie::czytanie(zmienna* z) : z(z) {
        if(!z)
            throw std::invalid_argument("Zmienne nie mogą być puste!");
    }

    czytanie::~czytanie() {
        delete z;
    }

    void czytanie::wykonaj() const {
        std::string str_val;

        while(true) {
            std::cout << "Wartość " << z->zapis() << " := ";
            std::cin >> str_val;

            try {
                int int_val = std::stoi(str_val);
                zmienna::ustaw(z->zapis(), int_val);
                break;
            }
            catch(const std::invalid_argument&) {
                std::cerr << "Podano niepoprawną wartością! Spróbuj ponownie." << std::endl;
            }
        }
    }

    std::string czytanie::zapis(int wciecie) const {
        return std::string(wciecie, ' ') + "read " + z->zapis() + ";";
    }
}
