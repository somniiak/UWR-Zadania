package wyrazenia;

public class Ln extends Wyrazenie {
    private Wyrazenie expr;

    public Ln(Wyrazenie expr) {
        this.expr = expr;
    }

    @Override
    protected int getPriority() {
        return 4;
    }

    @Override
    public double oblicz() {
        return Math.log(expr.oblicz());
    }

    @Override
    public String toString() {
        return "ln(" + expr + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
