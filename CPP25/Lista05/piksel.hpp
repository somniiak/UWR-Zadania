#ifndef PIKSEL_H
#define PIKSEL_H

#include <ostream>

class piksel
{
    private:
        int x, y;

    protected:
        static const int screen_width = 1920; // HDTV1080 (1920x1080)
        static const int screen_height = 1080;

    public:
        piksel();
        piksel(int nx, int ny);
        void set_x(int nx);
        void set_y(int ny);
        int get_x() const;
        int get_y() const;
        int distance_left();
        int distance_right();
        int distance_top();
        int distance_bottom();
        static double distance(const piksel* p1, const piksel* p2);
        static double distance(const piksel& p1, const piksel& p2);
        friend std::ostream& operator<<(std::ostream &out, const piksel &p);
};

#endif