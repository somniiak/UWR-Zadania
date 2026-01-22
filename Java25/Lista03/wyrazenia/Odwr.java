package wyrazenia;

public class Odwr extends Wyrazenie {
    private Wyrazenie expr;

    public Odwr(Wyrazenie expr) {
        this.expr = expr;
    }

    @Override
    protected int getPriority() {
        return 3;
    }

    @Override
    public double oblicz() {
        return 1 / expr.oblicz();
    }

    @Override
    public String toString() {
        if (expr.getPriority() < getPriority())
            return "! (" + expr + ")";
        return "! " + expr;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
