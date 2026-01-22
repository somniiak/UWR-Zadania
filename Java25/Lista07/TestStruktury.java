import structures.SimpleList;

import java.util.Date;

public class TestStruktury {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        SimpleList<Integer> IntegerList = new SimpleList<>();

        IntegerList.insert(10, 0);
        IntegerList.insert(30, 1);
        IntegerList.insert(20, 1);
        IntegerList.insert(40, 3);
        IntegerList.insert(50, 4);
        IntegerList.remove(Integer.valueOf(50));

        System.out.println("IntegerList: " + IntegerList);
        System.out.println("Min: " + IntegerList.min() + ", Max: " + IntegerList.max());
        System.out.println("Czy zawiera 20: " + IntegerList.search(20));
        System.out.println("Index 40: " + IntegerList.index(40));

        SimpleList<String> StringList = new SimpleList<>();

        StringList.insert("clojure", 0);
        StringList.insert("java", 0);
        StringList.insert("kotlin", 0);

        for (String cur : StringList)
            System.out.println(cur);

        System.out.println("Min: " + StringList.min() + ", Max: " + StringList.max());

        SimpleList<Date> DateList = new SimpleList<>();

        DateList.insert(new Date(121, 0, 15), 0);
        DateList.insert(new Date(122, 5, 20), 1);
        DateList.insert(new Date(120, 11, 5), 0);
        DateList.insert(new Date(123, 2, 10), 3);
        DateList.insert(new Date(119, 7, 25), 2);

        System.out.println("Najwcześniejsza data: " + DateList.min());
        System.out.println("Najpóźniejsza data: " + DateList.max());
    }
}
