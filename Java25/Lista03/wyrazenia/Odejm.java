package wyrazenia;

public class Odejm extends Wyrazenie {
    private Wyrazenie expr1;
    private Wyrazenie expr2;

    public Odejm(Wyrazenie expr1, Wyrazenie expr2) {
        this.expr1 = expr1;
        this.expr2 = expr2;
    }

    @Override
    protected int getPriority() {
        return 1;
    }

    @Override
    public double oblicz() {
        return expr1.oblicz() - expr2.oblicz();
    }

    @Override
    public String toString() {
        String left = (expr1.getPriority() < getPriority()) ? "(" + expr1 + ")" : "" + expr1;
        String right = (expr2.getPriority() <= getPriority()) ? "(" + expr2 + ")" : "" + expr2;
        return left + " - " + right;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
