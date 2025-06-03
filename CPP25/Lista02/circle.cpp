#include <stdexcept>
#include <utility>
#include <cmath>

#include "circle.hpp"
#include "point.hpp"

Circle::Circle() {
    center.set_pos(0, 0);
    radius = 1;
}

Circle::Circle(double nx, double ny, double nr) {
    if (nr <= 0)
        throw std::invalid_argument("Wartość promienia musi być nieujemna");

    else {
        center.set_pos(nx, ny);
        radius = nr;
    }
}

void Circle::set_center(double nx, double ny) {
    center.set_pos(nx, ny);
}

std::pair<double, double> Circle::get_center() {
    return {center.get_pos().first, center.get_pos().second};
}

void Circle::set_radius(double nr) {
    if (nr <= 0)
        throw std::invalid_argument("Wartość promienia musi być nieujemna");
    else
        radius = nr;
}

double Circle::get_radius() {
    return radius;
}

double Circle::area() {
    return 3.14159265 * radius * radius;
}

double Circle::circumference() {
    return 3.14159265 * 2 * radius;
}

void Circle::shift_by(Vector sv) {
    center.shift_by(sv);
}

void Circle::rotate_by(Point sp, double angle) {
    center.rotate_by(sp, angle);
}

void Circle::point_symmetry(Point sp) {
    center.point_symmetry(sp);
}

void Circle::axial_symmetry(Line sl) {
    center.axial_symmetry(sl);
}

bool Circle::is_in_circle(Point sp) {
    if (
        std::pow(sp.get_pos().first, 2) + std::pow(center.get_pos().first, 2) +
        std::pow(sp.get_pos().second, 2) + std::pow(center.get_pos().second, 2) <=
        std::pow(radius, 2)
    )
        return true;
    else
        return false;
}

bool Circle::is_in_circle(double sx, double sy) {
    if (
        std::pow(sx, 2) + std::pow(center.get_pos().first, 2) +
        std::pow(sy, 2) + std::pow(center.get_pos().second, 2) <=
        std::pow(radius, 2)
    )
        return true;
    else
        return false;
}

bool is_inside(Circle c1, Circle c2)
{
    double d = std::sqrt(
        std::pow(c1.get_center().first - c2.get_center().first, 2) +
        std::pow(c1.get_center().second - c2.get_center().second, 2)
    );

    return (d + c1.get_radius() <= c2.get_radius());
}

bool is_disjoint(Circle c1, Circle c2)
{
    double d = std::sqrt(
        std::pow(c1.get_center().first - c2.get_center().first, 2) +
        std::pow(c1.get_center().second - c2.get_center().second, 2)
    );

    return (d >= c1.get_radius() + c2.get_radius());
}