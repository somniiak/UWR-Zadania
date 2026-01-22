package figury;

public class Trojkat {
    private Punkt a;
    private Punkt b;
    private Punkt c;

    public Trojkat(Punkt p1, Punkt p2, Punkt p3) {
        if (p1 == p2 || p2 == p3 || p1 == p3)
            throw new java.lang.IllegalArgumentException(
                "Trójkąt musi być zbudowany z trzech różnych punktów!"
            );
        
        if (Punkt.areCollinear(p1, p2, p3))
            throw new java.lang.IllegalArgumentException(
                "Trójkąt musi być zbudowany z trzech niewspółliniowych punktów!"
            );

        a = p1; b = p2; c = p3;
    }

    // Przesunięcie o wektor
    public void przesun(Wektor v) {
        a.przesun(v); b.przesun(v); c.przesun(v);
    }

    // Obrót wokół punktu
    public void obroc(Punkt p, double d) {
        a.obroc(p, d); b.obroc(p, d); c.obroc(p, d);
    }

    // Symetria względem prostej
    public void odbij(Prosta p) {
        a.odbij(p); b.odbij(p); c.odbij(p);
    }

    @Override
    public String toString() {
        return "(" + a + ", " + b + ", " + c + ")";
    }
}
