public class Pair implements Cloneable {
    public final String key;
    private double value;

    public Pair(String key, double value) {
        if (key == null)
            throw new IllegalArgumentException("Klucz nie może być null");
        if (key.isBlank())
            throw new IllegalArgumentException("Klucz nie może być pusty");
        if (!key.matches("[a-z]+"))
            throw new IllegalArgumentException("Klucz może zawierać tylko małe litery alfabetu angielskiego");

        this.key = key;
        this.value = value;
    }

    public void set(double new_value) {
        value = new_value;
    }

    public double get() {
        return value;
    }

    @Override
    public String toString() {
        return "Pair(" + key + ", " + value + ")"; 
    }

    @Override
    public boolean equals(Object o) {
        if (this == o)
            return true;
        if (!(o instanceof Pair))
            return false;
        Pair other = (Pair) o;
        return key.equals(other.key);
    }

    // metoda zwraca Pair bez rzutowania
    @Override
    public Pair clone() {
        try {
            return (Pair) super.clone();
        }
        catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}