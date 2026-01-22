import wyrazenia.*;

public class TestWyrazenia {
    public static void main(String[] args) {
        // Wyrażenie 1: 7.2 + (x * 2.4)
        Zmienna.Ustaw("x", new Liczba(1.618));
        Wyrazenie w1 = new Dodaj(
            new Liczba(7.2),
            new Mnoz(
                new Zmienna("x"),
                new Liczba(2.4)
            )
        );
        System.out.println(w1 + " = " + w1.oblicz());

        // Wyrażenie 2: exp(ln(5)) + 3 * log(e, x)
        Zmienna.Ustaw("x", Stala.E);
        Wyrazenie w2 = new Dodaj(
            new Exp(
                new Ln(
                    new Liczba(5.0)
                )
            ),
            new Mnoz(
                new Liczba(3.0),
                new Log(
                    Stala.E,
                    new Zmienna("x")
                )
            )
        );
        System.out.println(w2 + " = " + w2.oblicz());

        // Wyrażenie 3: ~(2 - x) * e
        Zmienna.Ustaw("x", new Odwr(Stala.E));
        Wyrazenie w3 = new Mnoz(
            new Przec(
                new Odejm(
                    new Liczba(2.0),
                    new Zmienna("x")
                )
            ),
            Stala.E
        );
        System.out.println(w3 + " = " + w3.oblicz());

        // Wyrażenie 4: (3 * π - 1) / (!x + 5)
        Zmienna.Ustaw("x", new Liczba(2));
        Wyrazenie w4 = new Dziel(
            new Odejm(
                new Mnoz(
                    new Liczba(3.0),
                    Stala.Pi
                ),
                new Liczba(1.0)
            ),
            new Dodaj(
                new Odwr(
                    new Zmienna("x")
                ),
                new Liczba(5.0)
            )
        );
        System.out.println(w4 + " = " + w4.oblicz());
    }
}
