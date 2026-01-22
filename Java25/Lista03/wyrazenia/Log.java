package wyrazenia;

public class Log extends Wyrazenie {
    private Wyrazenie expr1;
    private Wyrazenie expr2;

    public Log(Wyrazenie expr1, Wyrazenie expr2) {
        this.expr1 = expr1;
        this.expr2 = expr2;
    }

    @Override
    protected int getPriority() {
        return 3;
    }

    @Override
    public double oblicz() {
        return Math.log(expr2.oblicz()) / Math.log(expr1.oblicz());
    }

    @Override
    public String toString() {
        return "log_{" + expr1 +"}(" + expr2 + ")";
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
