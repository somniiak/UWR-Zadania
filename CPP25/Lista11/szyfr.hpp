#ifndef SZYFR_HPP
#define SZYFR_HPP

#include <string>

class szyfr
{
    public:
        static char szyfrujZnak(char c, int key) {
            if (std::isupper(c))
                return 'A' + (c - 'A' + key) % 26;
            else if (std::islower(c))
                return 'a' + (c - 'a' + key) % 26;
            return c;
        }

        static std::string szyfrujTekst(std::string text, int key) {
            for (char& c : text)
                c = szyfrujZnak(c, key);
            return text;
        }
};

#endif