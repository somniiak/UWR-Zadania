public class ArraySetVar extends SetVar {
    protected Pair[] vars;
    protected int siz;

    public ArraySetVar(int capacity) {
        vars = new Pair[capacity];
        siz = 0;
    }

    @Override
    public void set(String k, double v) {
        for (int i = 0; i < siz; i++) {
            if (vars[i].key.equals(k)) {
                vars[i].set(v);
                return;
            }
        }

        if (siz >= vars.length)
            throw new IllegalStateException("Brak miejsca w tablicy");

        vars[siz++] = new Pair(k, v);
    }

    @Override
    public double get(String k) {
        for (int i = 0; i < siz; i++) {
            if (vars[i].key.equals(k)) {
                return vars[i].get();
            }
        }
        throw new IllegalArgumentException("Nie znaleziono klucza: " + k);
    }

    @Override
    public void del(String k) {
        for (int i = 0; i < siz; i++) {
            if (vars[i].key.equals(k)) {
                vars[i] = vars[siz - 1];
                vars[--siz] = null;
                return;
            }
        }
    }

    @Override
    public boolean search(String k) {
        for (int i = 0; i < siz; i++)
            if (vars[i].key.equals(k))
                return true;
        return false;
    }

    @Override
    public int size() {
        return siz;
    }

    @Override
    public void clear() {
        for (int i = 0; i < siz; i++)
            vars[i] = null;
        siz = 0;
    }

    @Override
    public String[] names() {
        String[] names = new String[siz];
        for (int i = 0; i < siz; i++)
            names[i] = vars[i].key;
        return names;
    }

    @Override
    public String toString() {
        return defaultToString();
    }
    
    @Override
    public ArraySetVar clone() {
        try {
            ArraySetVar copy = (ArraySetVar) super.clone();
            copy.vars = new Pair[vars.length];
            for (int i = 0; i < siz; i++)
                copy.vars[i] = vars[i].clone();
            return copy;
        }
        catch (CloneNotSupportedException e) {
            throw new AssertionError();
        }
    }
}
