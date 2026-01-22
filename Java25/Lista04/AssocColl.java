public interface AssocColl {
    void set(String k, double v);
    double get(String k);
    boolean search(String k);
    String[] names();

    default String defaultToString() {
        var res = new StringBuilder();
        res.append("{");
        String[] keys = names();
        for (int i = 0; i < keys.length; i++) {
            res.append(keys[i]);
            res.append(" = ");
            res.append(get(keys[i]));
            if (i < keys.length - 1)
                res.append(", ");
        }
        res.append("}");
        return res.toString();
    }
}