#ifndef LINE
#define LINE

class Line
{
    private:
        double A, B, C;

    public:
        Line();
        Line(double nA, double nB, double nC);
        double get_A();
        double get_B();
        double get_C();
};

#endif