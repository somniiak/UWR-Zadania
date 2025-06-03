#ifndef KOLORNAZ_H
#define KOLORNAZ_H

#include <string>
#include "kolor.hpp"

class kolornazwany : public virtual kolor
{
    private:
        std::string nazwa;

    public:
        kolornazwany();
        kolornazwany(ushort red, ushort green, ushort blue, std::string value);
        std::string get_name() const;
        void set_name(std::string value);
        friend std::ostream& operator<<(std::ostream &out, const kolornazwany &k);
};

#endif