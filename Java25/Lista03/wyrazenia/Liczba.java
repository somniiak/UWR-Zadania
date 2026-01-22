package wyrazenia;

public class Liczba extends Wyrazenie {
    public static final Liczba ZERO = new Liczba(0.0);
    public static final Liczba JEDEN = new Liczba(1.0);

    private double value;

    public Liczba(double value) {
        this.value = value;
    }

    @Override
    protected int getPriority() {
        return 4;
    }

    @Override
    public double oblicz() {
        return value;
    }

    @Override
    public String toString() {
        return Double.toString(value);
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Wyrazenie)
            return oblicz() == ((Wyrazenie) obj).oblicz();
        return false;
    }
}
