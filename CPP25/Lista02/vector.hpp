#ifndef VECTOR_HPP
#define VECTOR_HPP

#include <utility>

class Vector
{
    private:
        double dx;
        double dy;

    public:
        Vector();
        Vector(double nx, double ny);
        void set_size(double nx, double ny);
        std::pair<double, double> get_size();
};

#endif