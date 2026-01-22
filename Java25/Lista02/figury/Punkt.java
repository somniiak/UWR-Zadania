package figury;

public class Punkt {
    private double x;
    private double y;

    public Punkt(double x, double y) {
        this.x = x; this.y = y;
    }

    // Przesunięcie o wektor
    public void przesun(Wektor v) {
        x += v.dx; y += v.dy;
    }

    // Obrót wokół punktu
    public void obroc(Punkt p, double d) {
        double dx = x - p.getX();
        double dy = y - p.getY();
        d *= Math.PI / 180;
        x = p.getX() + dx * Math.cos(d) - dy * Math.sin(d);
        y = p.getY() + dx * Math.sin(d) + dy * Math.cos(d);
    }

    // Symetria względem prostej
    public void odbij(Prosta p) {
        double new_x = (p.b * p.b - p.a * p.a) * x;
        new_x -= 2 * (p.a * p.b * y + p.a * p.c);
        new_x /= p.a * p.a + p.b * p.b;

        double new_y = (p.a * p.a - p.b * p.b) * y;
        new_y -= 2 * (p.a * p.b * x + p.b * p.c);
        new_y /= p.a * p.a + p.b * p.b;

        x = new_x; y = new_y;
    }

    // Współliniowość punktów
    public static boolean areCollinear(Punkt p1, Punkt p2, Punkt p3) {
        return (
            (p2.getY() - p1.getY()) * (p3.getX() - p2.getX()) ==
            (p3.getY() - p2.getY()) * (p2.getX() - p1.getX())
        );
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    @Override
    public String toString() {
        return "(" + String.format("%.2f", x) + ", " + String.format("%.2f", y) + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Punkt) {
            return (
                getX() == ((Punkt)obj).getX() &&
                getX() == ((Punkt)obj).getY()
            );
        }
        return false;
    }
}
