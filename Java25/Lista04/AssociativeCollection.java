public interface AssociativeCollection extends AssocColl, Cloneable {
    void del(String k);
    int size();

    @Override
    default String defaultToString() {
        var res = new StringBuilder();
        res.append("{");
        String[] keys = names();
        for (int i = 0; i < keys.length; i++) {
            res.append(keys[i]);
            res.append(" := ");
            res.append(get(keys[i]));
            if (i < keys.length - 1)
                res.append("; ");
        }
        res.append("}");
        return res.toString();
    }
}
