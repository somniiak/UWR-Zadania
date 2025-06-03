#ifndef CIRCLE_HPP
#define CIRCLE_HPP

#include <utility>
#include "point.hpp"
#include "vector.hpp"
#include "line.hpp"

class Circle
{
    private:
        double radius;
        Point center;

    public:
        Circle();
        Circle(double nx, double ny, double nr);
        void set_center(double nx, double ny);
        std::pair<double, double> get_center();
        void set_radius(double nr);
        double get_radius();
        double area();
        double circumference();
        void shift_by(Vector sv);
        void rotate_by(Point sp, double angle);
        void point_symmetry(Point sp);
        void axial_symmetry(Line sl);
        bool is_in_circle(Point sp);
        bool is_in_circle(double sx, double sy);
};

bool is_inside(Circle c1, Circle c2);
bool is_disjoint(Circle c1, Circle c2);

#endif  