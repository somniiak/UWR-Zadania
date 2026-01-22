package figury;

public class Wektor {
    public final double dx;
    public final double dy;

    public Wektor() {
        this.dx = 0; this.dy = 0;
    }

    public Wektor(double dx, double dy) {
        this.dx = dx; this.dy = dy;
    }

    // Składanie wektorów
    public static Wektor addVectors(Wektor v1, Wektor v2) {
        return new Wektor(v1.dx + v2.dx, v1.dy + v2.dy);
    }

    @Override
    public String toString() {
        return "[" + String.format("%.2f", dx) + ", " + String.format("%.2f", dy) + "]";
    }
}
