#include <iostream>

#include "wejscie.hpp"
#include "wyjscie.hpp"

int main(int argc, char **argv)
{
    std::string plikWej = argv[1];
    std::string plikWyj = argv[2];
    int klucz = std::stoi(argv[3]);

    try {
        wejscie in(plikWej);
        wyjscie out(plikWyj);

        in.ustawKlucz(klucz);
        out.ustawKlucz(klucz);

        while (true) {
            std::string linia;
            try { linia = in.czytaj(); }
            catch (std::ios_base::failure&) { break; }
            out.pisz(linia);
        }
    }

    catch (const std::exception& e) {
        std::cerr << "Błąd: " << e.what() << '\n';
        return 1;
    }

    return 0;
}