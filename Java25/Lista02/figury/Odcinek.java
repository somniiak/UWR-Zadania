package figury;

public class Odcinek {
    private Punkt a;
    private Punkt b;

    public Odcinek(Punkt p1, Punkt p2) {
        if (p1 == p2)
            throw new java.lang.IllegalArgumentException(
                "Odcinek musi być zbudowany z dwóch różnych punktów!"
            );

        a = p1; b = p2;
    }

    // Przesunięcie o wektor
    public void przesun(Wektor v) {
        a.przesun(v); b.przesun(v);
    }

    // Obrót wokół punktu
    public void obroc(Punkt p, double d) {
        a.obroc(p, d); b.obroc(p, d);
    }

    // Symetria względem prostej
    public void odbij(Prosta p) {
        a.odbij(p); b.odbij(p);
    }

    @Override
    public String toString() {
        return "(" + a + ", " + b + ")";
    }
}
