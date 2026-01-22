package wyrazenia;

public class Sin extends Wyrazenie {
    private Wyrazenie expr;

    public Sin(Wyrazenie expr) {
        this.expr = expr;
    }

    @Override
    protected int getPriority() {
        return 3;
    }

    @Override
    public double oblicz() {
        return Math.sin(expr.oblicz());
    }

    @Override
    public String toString() {
        return "sin(" + expr + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
