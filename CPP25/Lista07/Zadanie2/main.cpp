#include <iostream>

#include "libwyrazenie.hpp"
#include "deklaracja.hpp"
#include "przypisanie.hpp"
#include "czytanie.hpp"
#include "pisanie.hpp"
#include "blok.hpp"
#include "if_stat.hpp"
#include "if_else_stat.hpp"
#include "while_stat.hpp"
#include "do_while_stat.hpp"

using namespace obliczenia;

int main(int argc, char **argv)
{
    zmienna n("n");
    zmienna p("p");
    zmienna wyn("wyn");

    instrukcja* program = new blok({
        new deklaracja("n"),
        new czytanie(&n),
        new if_else_stat(
            new mniejsze(&n, new liczba(2)),
            new pisanie(new liczba(0)),
            new blok({
                new deklaracja("p"),
                new przypisanie(&p, new liczba(2)),
                new deklaracja("wyn"),
                new while_stat(
                    new mniejsze_rowne(new mnozenie(&p, &p), &n),
                    new blok({
                        new if_stat(
                            new rowne(new modulo(&n, &p), new liczba(0)),
                            new blok({
                                new przypisanie(&wyn, &p),
                                new przypisanie(&p, &n)
                            })
                        ),
                        new przypisanie(&p, new dodawanie(&p, new liczba(1)))
                    })
                ),
                new if_else_stat(
                    new wieksze(&wyn, new liczba(0)),
                    new pisanie(new liczba(0)),
                    new pisanie(new liczba(1))
                )
            })
        )
    });

    std::cout << "Program testujący pierwszość liczby:\n";
    std::cout << program->zapis() << std::endl;
    program->wykonaj();

    return 0;
}
