#include <iostream>
#include "circle.hpp"
#include "point.hpp"
#include "vector.hpp"
#include "line.hpp"

void print_circle_info(Circle crc);
void print_point_info(Point pnt);

int main(int argc, char **argv)
{
    // Koło o środku (5, 2) i promieniu 3
    Circle kolo{5, 2, 3};
    // Pole koła
    std::cout << "Pole: " << kolo.area() << std::endl;
    // Obwód koła
    std::cout << "Obwód: " << kolo.circumference() << std::endl;
    // Zmiana współrzędnych środka i promienia
    print_circle_info(kolo);
    kolo.set_center(-2, 1);
    kolo.set_radius(5);
    print_circle_info(kolo);
    // Zawieranie okręgów
    if (is_inside(Circle{0, 1, 1}, Circle{0, 0, 2}))
        std::cout << "Circle{0, 2, 1} zawiera się w Circle{0, 0, 2}.\n";
    else
        std::cout << "Circle{0, 2, 1} nie zawiera się w Circle{0, 0, 2}.\n";
    // Rozłączność okręgów
    if (is_disjoint(Circle{0, 0, 1}, Circle{2, 0, 1}))
        std::cout << "Circle{0, 0, 1} oraz Circle{2, 0, 1} są rozłączne.\n";
    else
        std::cout << "Circle{0, 0, 1} oraz Circle{2, 0, 1} nie są rozłączne.\n";
    // Przesunięcie o wektor
    kolo.shift_by(Vector{-3, 7});
    print_circle_info(kolo);
    // Obrót wokół punktu o kąt
    kolo.rotate_by(Point{2, -1}, 90);
    print_circle_info(kolo);
    // Symetria środkowa
    kolo.point_symmetry(Point{1, 2});
    print_circle_info(kolo);
    //Symetria osiowa
    kolo.axial_symmetry(Line{4, 3, 0});
    print_circle_info(kolo);

    // Punkt (5, 2)
    Point punkt{5, 2};
    // Odległość pomiędzy punktami
    std::cout << "Odległość pomiędzy (1, 1) i (0, 0): ";
    std::cout << distance(Point{1, 1}, Point{0, 0}) << std::endl;
    // Zmiana współrzędnych
    punkt.set_pos(4, 2);
    print_point_info(punkt);
    // Przesunięcie o wektor
    punkt.shift_by(Vector{4, -2});
    print_point_info(punkt);
    // Obrót wokół punktu o kąt
    punkt.rotate_by(Point{2, -1}, 90);
    print_point_info(punkt);
    // Symetria środkowa
    punkt.point_symmetry(Point{1, 2});
    print_point_info(punkt);
    //Symetria osiowa
    punkt.axial_symmetry(Line{2, 1, 3});
    print_point_info(punkt);
    // Błąd: niedodatni promień
    // kolo.set_radius(-1);
    // Błąd: A i B zerowe
    // Line linia(0, 0, 1);

    return 0;
}

void print_circle_info(Circle crc)
{
    std::cout << "Środek: (";
    std::cout << crc.get_center().first << ", "; 
    std::cout << crc.get_center().second << "); R = ";
    std::cout << crc.get_radius() << ";" << std::endl;
}

void print_point_info(Point pnt)
{
    std::cout << "XY: (";
    std::cout << pnt.get_pos().first << ", "; 
    std::cout << pnt.get_pos().second << ")" << std::endl;
}