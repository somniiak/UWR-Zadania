package wyrazenia;

public class Zmienna extends Wyrazenie {
    private static java.util.HashMap<String, Wyrazenie> variables =
        new java.util.HashMap<>();

    private String variable;

    public Zmienna(String variable) {
        if (!variables.containsKey(variable))
            throw new Error("Niezadeklarowana zmienna!");
        this.variable = variable;
    }

    public static void Ustaw(String variable, Wyrazenie expr) {
        variables.put(variable, new Liczba(expr.oblicz()));
    }

    @Override
    protected int getPriority() {
        return 4;
    }

    @Override
    public double oblicz() {
        return variables.get(variable).oblicz();
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
