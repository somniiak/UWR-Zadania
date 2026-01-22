package wyrazenia;

public abstract class Wyrazenie implements Obliczalny {
    public static Liczba suma (Wyrazenie... wyr) {
        Liczba res = new Liczba(0);

        for (Wyrazenie w : wyr)
            res = new Liczba(res.oblicz() + w.oblicz());
        
        return res;
    }
    
    public static Liczba iloczyn (Wyrazenie... wyr) {
        Liczba res = new Liczba(1);

        for (Wyrazenie w : wyr)
            res = new Liczba(res.oblicz() * w.oblicz());
        
        return res;
    }

    protected abstract int getPriority();

    public abstract double oblicz();

    public abstract String toString();

    public abstract boolean equals(Object obj);
}
