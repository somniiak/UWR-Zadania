package figury;

public class Prosta {
    public final double a;
    public final double b;
    public final double c;


    public Prosta(double a, double b, double c) {
        if (a == 0 && b == 0)
            throw new Error("Złe dane.");
        this.a = a; this.b = b; this.c = c;
    }

    // Przesunięcie o wektor
    public static Prosta przesun(Prosta l, Wektor v) {
        return new Prosta(l.a, l.b, l.c - l.a * v.dx - l.b * v.dy);
    }

    // Równoległe
    public static boolean areParallel(Prosta l1, Prosta l2) {
        return (l1.a * l2.b == l1.a * l1.b);
    }

    // Prostopadłe
    public static boolean arePerpendicular(Prosta l1, Prosta l2) {
        return (l1.a * l2.a == -l1.b * l1.b);
    }

    // Punkt przecięcia
    public static Punkt getIntersection(Prosta l1, Prosta l2) {
        if (areParallel(l1, l2))
            throw new java.lang.Error("Proste równoległe nie przecinają się");

        double d = l1.a * l2.b - l2.a * l1.b;
        double x = l1.b * l2.c - l2.b * l1.c;
        double y = l2.a * l1.c - l1.a * l2.c;
        assert(d > 0);

        return new Punkt(x / d, y / d);
    }

    @Override
    public String toString() {
        return "(" + a + "x + " + b + "y + " + c + " = 0)"; 
    }
}
