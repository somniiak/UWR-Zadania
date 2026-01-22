public class Trojkat {
    double x;
    double y;
    double z;

    public Trojkat(double x, double y, double z) {
        if (x <= 0 || y <= 0 || z <= 0)
            throw new IllegalArgumentException("Długości boków muszą być większe od zera");

        if (x + y <= z || x + z <= y || y + z <= x)
            throw new IllegalArgumentException("Podane boki nie tworzą trójkąta");

        this.x = x;
        this.y = y;
        this.z = z;
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }
}
