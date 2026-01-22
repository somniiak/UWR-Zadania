public class TestZbiory {
    public static void main(String[] args) {
        ArraySetVar arr = new ArraySetVar(10);
        arr.set("x", 10.5);
        arr.set("y", 20.3);
        arr.set("z", 30.7);

        System.out.println(arr);
        System.out.println("Rozmiar: " + arr.size());

        ArraySetVar arrCopy = arr.clone();
        arrCopy.set("x", 100.0);

        System.out.println("Oryginalny: " + arr);
        System.out.println("Sklonowany: " + arrCopy);

        PairProb prob = new PairProb("prob", 0.75);
        System.out.println(prob);

        try {
            prob.set(1.5);
        }
        catch (IllegalArgumentException e) {
            System.out.println("Wyjątek: " + e.getMessage());
        }
    }
}
