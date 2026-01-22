package rozgrywka;

import wyjatki.*;
import obliczenia.Wymierna;

import java.util.Scanner;
import java.util.logging.Logger;
import java.util.logging.LogManager;
import java.io.FileInputStream;
import java.io.IOException;

public class Gra {
    // https://stackoverflow.com/a/16448421
    private static final Logger logger = Logger.getLogger(Gra.class.getName());

    private int zakres;
    private Wymierna liczba;
    private int maksIloscProb;
    private int licznikProb;
    private long timeStart;
    private String playerName;
    private static final Scanner input = new Scanner(System.in);

    // https://stackoverflow.com/q/960099
    static {
        try {
            LogManager.getLogManager().readConfiguration(new FileInputStream("logging.properties"));
        } catch (IOException e) {
            System.err.println("Nie udało się wczytać konfiguracji logowania: " + e.getMessage());
        }
    }

    public void setName() {
        System.out.print("Podaj swoje imię: ");
        playerName = input.nextLine().trim();
        logger.info("Rozpoczęto rozgrywkę: " + playerName);
    }

    public void start(int z) throws ZgadywankaException {
        if (z < 5 || z > 20)
            throw new ZakresException("Liczba określająca zakres " +
                "wartości rozgrywki powinna być większa lub równa 4");

        zakres = z;

        // Z równania 0 < a < b <= z, (gdzie a, b, z ∈ Z) otrzymujemy:
        // a ∈ [1; z - 1], b ∈ [a + 1; z]. Math.random -> [0; 1).

        // int a = (int) (Math.random() * (z - 1) + 1);
        // int b = (int) (Math.random() * (z - a) + a + 1);
        // assert(0 < a && a < b && b <= z);

        int a = (int) (Math.random() * zakres) + 1;
        int b = (int) (Math.random() * zakres) + 1;
        assert(a < b) : "Licznik większy od mianownika!";

        liczba = new Wymierna(a, b);
        maksIloscProb = (int) Math.ceil(3 * Math.log(z));
        licznikProb = 0;

        logger.info("Rozpoczęto grę z zakresem: " + z);
        logger.info("Liczba do odgadnięcia: " + liczba);
        logger.info("Maksymalna liczba prób: " + maksIloscProb);

        timeStart = System.currentTimeMillis();

        run();
    }

    private void run() {
        while (licznikProb < maksIloscProb) {
            System.out.println(
                "Pozostałe próby: " + (maksIloscProb - licznikProb));
            System.out.print("Podaj liczbę: ");

            String line = input.nextLine().trim();
            logger.info("Próba " + (licznikProb + 1) + " - wejście: " + line);

            // Sprawdzamy czy użytkownik się poddał
            if (line.equals("exit")) {
                forfeit(); return;
            }

            try {
                Wymierna guess = parseWymierna(line);
                int cmp = guess.compareTo(liczba);
                licznikProb++;

                if (cmp == 0) {                        
                    success();
                    return;
                } else if (cmp < 0) {
                    System.out.println("Za mało!\n");
                } else {
                    System.out.println("Za dużo!\n");
                }
            } catch (Exception e) {
                logger.info(e.getMessage());
                System.out.println(e.getMessage() + "\n");
            }
        }

        // Przekroczenie liczby prób
        fail();
    }

    private Wymierna parseWymierna(String line) throws ZgadywankaException {
        // Tablica liczb typu string oddzielonych innymi znakami
        String[] parts = line.split("[^\\d]+");

        // Sprawdzamy czy użytkownik podał dwie liczby
        if (parts.length != 2)
            throw new ZleDaneException("Niepoprawne dane wejściowe. Podaj dwie liczby.");

        int l = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);

        if (m == 0)
            throw new MianownikException("Mianownik nie może być równy 0.");
        if (m > zakres)
            throw new MianownikException("Mianownik przekracza dopuszczalny zakres.");
        if (l <= 0 || l >= m)
            throw new ZakresException("Liczba wymierna musi należeć do przedziału (0; 1).");

        logger.info("Próba " + (licznikProb + 1) + " - sparsowano: " + line + " -> " + l + "/" + m);
        return new Wymierna(l, m);
    }

    private void forfeit() {
        System.out.println("Rezygnacja! Szukana liczba to: " + liczba);
        logger.info("Gracz poddał się po " + licznikProb + " próbach.");
        end("AUTOMAT");
    }

    private void fail() {
        System.out.println("Porażka! Szukana liczba to: " + liczba);
        logger.info("Gracz przegrał wyczerpawszy wszystkie próby");
        end("AUTOMAT");

    }

    private void success() {
        System.out.println("Sukces! Odgadnięto liczbę: " + liczba + " w " + licznikProb + " próbach!");
        logger.info("Gracz wygrał w " + licznikProb + " próbach");
        end(playerName);
    }

    private void end(String winner) {
        input.close();
        logger.info("Runda zakończona - zwycięzca: " + winner +", czas trwania: " +
            ((System.currentTimeMillis() - timeStart) / 1000) + "s");
    }
}
