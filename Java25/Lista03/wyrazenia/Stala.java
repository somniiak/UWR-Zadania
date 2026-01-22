package wyrazenia;

public class Stala extends Wyrazenie {
    public static final Stala Pi = new Stala("π", new Liczba(Math.PI));
    public static final Stala E = new Stala("e", new Liczba(Math.exp(1)));

    private String variable;
    private Wyrazenie expr; 

    public Stala(String variable, Wyrazenie expr) {
        this.variable = variable;
        this.expr = expr;
    }

    @Override
    protected int getPriority() {
        return 4;
    }

    @Override
    public double oblicz() {
        return expr.oblicz();
    }

    @Override
    public String toString() {
        return variable;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
