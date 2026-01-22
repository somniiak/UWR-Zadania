package obliczenia;

/**
 * Klasa reprezentująca liczby Wymierne w postaci ułamka
 * nieskracalnego - uproszczonego za pomocą algorytmu Euklidesa,
 * z liczbami ujemnymi występującymi wyłącznie w liczniku. Licznik i
 * mianownik są zapisywane w postaci liczb całkowitych.
 * 
 * @author 353548
 * @version 1.0
*/

public class Wymierna implements Comparable<Wymierna>{
    /** Licznik liczby wymiernej. */
    private int licznik;

    /** Mianownik liczby wymiernej. */
    private int mianownik = 1;

    /**
     * Konstruktor bezargumentowy delegatowy. Tworzy 0 / 1.
     */
    public Wymierna() {
        this(0, 1);
    }

    /**
     * Konstruktor jednoargumentowy delegatowy. Tworzy l / 1.
     * @param l licznik
     */
    public Wymierna(int l) {
        this(l, 1);
    }

    /**
     * Konstruktor dwuparametrowy
     * @param l licznik
     * @param m mianownik
     */
    public Wymierna(int l, int m) {
        normalize(l, m);
    }

    /**
     * Normalizacja dwóch liczb całkowitych - skrócenie przez
     * wspólne NWD i przeniesienie znaku minus do licznika.
     * @param l licznik
     * @param m mianownik
     * @throws IllegalArgumentException mianownik nie może być zerowy
     */
    private void normalize(int l, int m) {
        if (m == 0)
            throw new IllegalArgumentException(
                "Mianownik nie może być zerem."
            );

        if (m < 0) {
            l = -l;
            m = -m;
        }

        int nwd = gcd(l, m);
        licznik = l / nwd;
        mianownik = m / nwd;

        assert mianownik > 0;
        assert gcd(licznik, mianownik) == 1;
    }

    /**
     * Reukurencyjna implementacja algorytmu Euklidesa do znajdowania NWD
     * dwóch liczb całkowitych. Wspiera także liczby ujemne.
     * @param a pierwsza liczba
     * @param b druga liczba
     * @return NWD(a, b)
     */
    private int gcd(int a, int b) {
        if (b == 0)
            return Math.max(a, -a);
        return gcd(b, a % b);
    }

    /**
     * Getter (licznik)
     * @return licznik
    */
    public int getLicznik() {
        return licznik;
    }

    /**
     * Getter (Mianownik)
     * @return mianownik
    */
    public int getMianownik() {
        return mianownik;
    }

    /**
     * Setter (Licznik)
     * @param l nowy licznik
    */
    public void setLicznik(int l) {
        normalize(l, mianownik);
    }

    /**
     * Setter (Mianownik)
     * @param m nowy mianownik
    */
    public void setMianownik(int m) {
        normalize(licznik, m);
    }

    /**
     * Dodawanie liczb wymiernych.
     * @param w1 pierwsza liczba wymierna
     * @param w2 druga liczba wymierna
     * @return suma w1 i w2
    */
    public static Wymierna add(Wymierna w1, Wymierna w2) {
        int w1_mian = w1.getMianownik();
        int w2_mian = w2.getMianownik();

        return new Wymierna(
            w1.getLicznik() * w2_mian + w2.getLicznik() * w1_mian,
            w1_mian * w2_mian
        );
    }

    /**
     * Odejmowanie liczb wymiernych.
     * @param w1 pierwsza liczba wymierna
     * @param w2 druga liczba wymierna
     * @return różnica w1 i w2
    */
    public static Wymierna sub(Wymierna w1, Wymierna w2) {
        int w1_mian = w1.getMianownik();
        int w2_mian = w2.getMianownik();

        return new Wymierna(
            w1.getLicznik() * w2_mian - w2.getLicznik() * w1_mian,
            w1_mian * w2_mian
        );
    }

    /**
     * Mnożenie liczb wymiernych.
     * @param w1 pierwsza liczba wymierna
     * @param w2 druga liczba wymierna
     * @return iloczyn w1 i w2
    */
    public static Wymierna mul(Wymierna w1, Wymierna w2) {
        return new Wymierna(
            w1.getLicznik() * w2.getLicznik(),
            w1.getMianownik() * w2.getMianownik()
        );
    }

    /**
     * Dzielenie liczb wymiernych.
     * @param w1 pierwsza liczba wymierna
     * @param w2 druga liczba wymierna
     * @return iloraz w1 i w2
     * @throws ArithmeticException nie można dzielić przez zero
    */
    public static Wymierna div(Wymierna w1, Wymierna w2) {
        if (w2.getLicznik() == 0)
            throw new ArithmeticException("Próba dzielenia przez zero.");
        return new Wymierna(
            w1.getLicznik() * w2.getMianownik(),
            w1.getMianownik() * w2.getLicznik()
        );
    }

    /**
     * Zwraca liczbę wymierną w postaci ciągu znaków.
     * @return "licznik / mianownik"
    */
    @Override
    public String toString() {
        return licznik + "/" + mianownik;
    }

    /**
     * Sprawdza czy dwie liczby wymierne mają jednakową wartość.
     * @param obj obiekt względem którego porównujemy
     * @return czy liczby są takie same
    */
    @Override
    public boolean equals(Object obj) {
        if (obj == this)
            return true;
        if (obj instanceof Wymierna other)
            return (
                getLicznik() == other.getLicznik() &&
                getMianownik() == other.getMianownik()
            );
        return false;
    }

    /**
     * Porównanie dwóch liczb wymiernych według ich wartości.
     * @param other liczba względem której porównujemy
     * @return -1, 0, 1 w zależności od wyniku
    */
    @Override
    public int compareTo(Wymierna other) {
        return Integer.compare(
            getLicznik() * other.getMianownik(),
            other.getLicznik() * getMianownik()
        );
    }
}
