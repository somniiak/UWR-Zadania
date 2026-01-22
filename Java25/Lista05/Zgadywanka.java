import rozgrywka.Gra;
import wyjatki.*;

public class Zgadywanka {
    public static void main(String[] args) throws ZgadywankaException {
        Gra gra = new Gra();
        try {
            gra.setName();
            gra.start(7);
        } catch (ZgadywankaException e) {
            System.err.println("Błąd gry: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Niespodziewany błąd: " + e.getMessage());
        }
    }
}