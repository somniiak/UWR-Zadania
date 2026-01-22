package wyrazenia;

public class Cos extends Wyrazenie {
    private Wyrazenie expr;

    public Cos(Wyrazenie expr) {
        this.expr = expr;
    }

    @Override
    protected int getPriority() {
        return 3;
    }

    @Override
    public double oblicz() {
        return Math.cos(expr.oblicz());
    }

    @Override
    public String toString() {
        return "cos(" + expr + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
