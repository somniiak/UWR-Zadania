public class PairProb extends Pair {
    public PairProb(String key, double value) {
        super(key, value);
        if (value < 0 || value > 1)
            throw new IllegalArgumentException(
                "Wartość PairProb musi należeć do przedziału [0;1]"
            );
    }

    @Override
    public void set(double value) {
        if (value < 0 || value > 1)
            throw new IllegalArgumentException(
                "Wartość PairProb musi należeć do przedziału [0;1]"
            );
        super.set(value);
    }

    @Override
    public String toString() {
        return "PairProb(" + key + ", " + get() + ")"; 
    }

    @Override
    public PairProb clone() {
        return (PairProb) super.clone();
    }
}
