package wyrazenia;

public class Exp extends Wyrazenie {
    private Wyrazenie expr;

    public Exp(Wyrazenie expr) {
        this.expr = expr;
    }

    @Override
    protected int getPriority() {
        return 3;
    }

    @Override
    public double oblicz() {
        return new Pot(Stala.E, expr).oblicz();
    }

    @Override
    public String toString() {
        return "exp(" + expr + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
