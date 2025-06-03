#ifndef POINT_HPP
#define POINT_HPP

#include <utility>
#include <cmath>
#include "vector.hpp"
#include "line.hpp"

class Point
{
    private:
        double x;
        double y;

    public:
        Point();
        Point(double nx, double ny);
        void set_pos(double nx, double ny);
        std::pair<double, double> get_pos();
        void shift_by(Vector nv);
        void rotate_by(Point np, double angle);
        void point_symmetry(Point sp);
        void axial_symmetry(Line sl);
};

double distance(Point p1, Point p2);

#endif