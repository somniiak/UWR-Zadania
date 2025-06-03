#ifndef PUNKT_H
#define PUNKT_H

class punkt
{
    private:
        double x;
        double y;

    public:
        punkt();
        punkt(int nx, int ny);
        double get_x();
        double get_y();
        void set_x(int nx);
        void set_y(int ny);
};

#endif