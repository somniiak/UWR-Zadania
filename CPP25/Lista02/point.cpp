#include <utility>
#include <cmath>

#include "point.hpp"
#include "vector.hpp"
#include "line.hpp"

Point::Point() {
    x = 0; y = 0;
}

Point::Point(double nx, double ny) {
    x = nx; y = ny;
}

void Point::set_pos(double nx, double ny) {
    x = nx; y = ny;
}

std::pair<double, double> Point::get_pos() {
    return {x, y};
}

void Point::shift_by(Vector nv) {
    x += nv.get_size().first;
    y += nv.get_size().second;
}

// Aby obrócić punkt o dany kąt względem innego punktu:
// 1. Przesunięcie punktu wokół którego obracamy, do początku
// układu współrzędnych. (Odjąć współrzędne punktu obrotu od
// współrzędnych punktu obracanego.)
// 2. Obróć punkt względem początku układuwspółrzędnych
// (0,0) o zadany kąt.
// 3. Po obrocie, przywróć punkt do jego oryginalnej pozycji,
// dodając współrzędne punktu obrotu z powrotem.

void Point::rotate_by(Point np, double angle) {
    // Konwersja na radiany
    angle = angle * 3.14159265 / 180;

    double x_shifted = x - np.get_pos().first;
    double y_shifted = y - np.get_pos().second;

    double x_rotated = x_shifted * cos(angle) - y_shifted * sin(angle);
    double y_rotated = x_shifted * sin(angle) + y_shifted * cos(angle);

    x = x_rotated + np.get_pos().first;
    y = y_rotated + np.get_pos().second;
}

void Point::point_symmetry(Point sp) {
    x = 2 * sp.get_pos().first - x;
    y = 2 * sp.get_pos().second - y;
}

void Point::axial_symmetry(Line sl) {
    double A = sl.get_A();
    double B = sl.get_B();
    double C = sl.get_C();
    
    double factor = 2 * (A * x + B * y + C) / (A * A + B * B);

    x -= A * factor;
    y -= B * factor;
}

double distance(Point p1, Point p2)
{
    return std::sqrt(
        std::pow(p1.get_pos().first - p2.get_pos().first, 2) + 
        std::pow(p1.get_pos().second - p2.get_pos().second, 2)
    );
}