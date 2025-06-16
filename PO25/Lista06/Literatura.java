// Artur Dzido
// Lista 6
// (OpenJDK 21)

import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.HashSet;

class Ksiazka implements Serializable {
    String tytul;
    int rokwydania;
    ArrayList<Pisarz> autorzy = new ArrayList<Pisarz>();

    Ksiazka(String tytul, Pisarz... autorzy) {
        this.tytul = tytul;
        for (Pisarz p : autorzy) {
            this.autorzy.add(p);
        }
    }

    @Override
    public String toString() {
        String info = "\"" + tytul + "\" - ";
        for(int i = 0; i < autorzy.size(); i++) {
            info += autorzy.get(i);
            if (i != autorzy.size() - 1) { info += ", "; }
        }
        return info;
    }
}

interface Obserwator
{
    void powiadomienie(Ksiazka k);
} 

class Pisarz implements Serializable {
    String pseudonim;
    int rokurodzenia;
    ArrayList<Obserwator> obserwatorzy = new ArrayList<Obserwator>();
    ArrayList<Ksiazka> ksiazki = new ArrayList<Ksiazka>();

    Pisarz (String pseudonim, Obserwator w)
    {
        this.pseudonim = pseudonim;
        this.obserwatorzy.add(w);
    }

    static MetodaPowiadamiania metoda = new KolejnoscPowiadamiania(); // Domyślna kolejność w poleceniu
    static void ustawMetode(MetodaPowiadamiania m) {
        metoda = m;
    }   

    void napisz(String tytul) {
        napiszKsiazke(tytul, this); // Pisze sam
    }

    static void napiszKsiazke(String tytul, Pisarz... autorzy) {
        Ksiazka ksiazka = new Ksiazka(tytul, autorzy);
        HashSet<Obserwator> unikalniObserwatorzy = new HashSet<>();
        for (Pisarz p : autorzy) {
            p.ksiazki.add(ksiazka);
            unikalniObserwatorzy.addAll(p.obserwatorzy);
            //metoda.powiadom(p.obserwatorzy, ksiazka);
        }
        metoda.powiadom(new ArrayList<>(unikalniObserwatorzy), ksiazka);
    }

    void dodajObserwatora(Obserwator o) {
        obserwatorzy.add(o);
    }

    void usunObserwatora(Obserwator o) {
        obserwatorzy.remove(o);
    }

    @Override public String toString() {
        return pseudonim;
    }
}

class Wydawnictwo implements Obserwator, Serializable {
    char nazwa;
    String siedziba;

    Wydawnictwo(char nazwa) {
        this.nazwa = nazwa;
    }

    void wydajKsiazke(Ksiazka ksiazka) {
        System.out.println("Wydawnicto " + this + " wydaje ksiazkę " + ksiazka);
    }

    public void powiadomienie(Ksiazka ksiazka) {
        if (ksiazka.tytul.charAt(0) == this.nazwa)
            this.wydajKsiazke(ksiazka);
    }

    @Override public String toString() {
        return Character.toString(nazwa);
    }
}

class Czytelnik implements Obserwator, Serializable
{
    public void powiadomienie(Ksiazka ksiazka) {
        System.out.println("Powiadomienie: nowa ksiazka " + ksiazka + "dodana do \"Do Przeczytania\"");
    }
}

class Recenzent implements Obserwator, Serializable
{
    String pseudonim;

    Recenzent(String pseudonim) {
        this.pseudonim = pseudonim;
    }

    void opublikujRecencje(Ksiazka ksiazka) {
        System.out.println(pseudonim + " recenzuje " + ksiazka);
    }

    public void powiadomienie(Ksiazka ksiazka) {
        opublikujRecencje(ksiazka);
    }

    @Override public String toString() {
        return pseudonim;
    }
}

class Biblioteka implements Obserwator, Serializable
{
    String nazwa;
    int wiek;

    Biblioteka(String nazwa, int wiek) {
        this.nazwa = nazwa;
        this.wiek = wiek;
    }

    void dodajDoZbioru(Ksiazka ksiazka) {
        System.out.println("Dodano " + ksiazka + " do zbiorów " + nazwa + ".");
    }

    public void powiadomienie(Ksiazka ksiazka) {
        dodajDoZbioru(ksiazka);
    }

    @Override public String toString() {
        return nazwa;
    }
}


interface MetodaPowiadamiania {
    void powiadom(ArrayList<Obserwator> obserwatorzy, Ksiazka ksiazka);
}

class KolejnoscPowiadamiania implements MetodaPowiadamiania {
    public void powiadom(ArrayList<Obserwator> obserwatorzy, Ksiazka ksiazka) {
        ArrayList<Obserwator> recenzenci = new ArrayList<>();
        ArrayList<Obserwator> wydawnictwa = new ArrayList<>();
        ArrayList<Obserwator> inni = new ArrayList<>();

        for (Obserwator o : obserwatorzy) {
            if (o instanceof Recenzent) recenzenci.add(o);
            else if (o instanceof Wydawnictwo) wydawnictwa.add(o);
            else inni.add(o);
        }

        for (Obserwator o : recenzenci) o.powiadomienie(ksiazka);
        for (Obserwator o : wydawnictwa) o.powiadomienie(ksiazka);
        for (Obserwator o : inni) o.powiadomienie(ksiazka);
    }
}

class Serializacja {
    static void zapisz(Object obiekt, String nazwaPliku) {
        try (ObjectOutputStream out = new ObjectOutputStream(new FileOutputStream(nazwaPliku))) {
            out.writeObject(obiekt);
            System.out.println("Zapisano obiekt do pliku: " + nazwaPliku);
        } catch (IOException e) {
            System.err.println("Błąd zapisu: " + e.getMessage());
        }
    }

    static Object odczytaj(String nazwaPliku) {
        try (ObjectInputStream in = new ObjectInputStream(new FileInputStream(nazwaPliku))) {
            return in.readObject();
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Błąd odczytu: " + e.getMessage());
            return null;
        }
    }
}


class Dane implements Serializable {
    ArrayList<Pisarz> pisarze;
    ArrayList<Ksiazka> ksiazki;
    ArrayList<Biblioteka> biblioteki;

    Dane(ArrayList<Pisarz> pisarze, ArrayList<Ksiazka> ksiazki, ArrayList<Biblioteka> biblioteki) {
        this.pisarze = pisarze;
        this.ksiazki = ksiazki;
        this.biblioteki = biblioteki;
    }
}

public class Literatura {
    public static void main(String[] args) {
        ArrayList<Pisarz> pisarze;
        ArrayList<Ksiazka> ksiazki;
        ArrayList<Biblioteka> biblioteki;

        File plik = new File("dane.ser");

        if (plik.exists()) {
            Dane dane = (Dane) Serializacja.odczytaj("dane.ser");

            if (dane != null) {
                pisarze = dane.pisarze;
                ksiazki = dane.ksiazki;
                biblioteki = dane.biblioteki;

                System.out.println("Dane odczytane z plików:");
                System.out.println("\nPisarze: ");
                for (Pisarz p : pisarze) System.out.print(p + ", ");
                System.out.println("\nKsiążki: ");
                for (Ksiazka k : ksiazki) System.out.print(k + ", ");
                System.out.println("\nBiblioteki :");
                for (Biblioteka b : biblioteki) System.out.print(b + ", ");
            }

            else {
                System.out.println("Błąd odczytu danych z pliku.");
            }
        }

        else {
            Pisarz.ustawMetode(new KolejnoscPowiadamiania());
            Wydawnictwo a = new Wydawnictwo('A');
            Pisarz aho = new Pisarz("aho", a);
            Pisarz hopcroft = new Pisarz("hopcroft", a);
            Pisarz ullmann = new Pisarz("ullmann", a);
            Recenzent recz = new Recenzent("Gal_Anonim");
            Biblioteka bibl = new Biblioteka("BUWr", 100);
            Czytelnik user2 = new Czytelnik();
            aho.dodajObserwatora(user2);
            aho.dodajObserwatora(bibl);
            aho.dodajObserwatora(recz);
            Pisarz.napiszKsiazke("AiSD", aho, hopcroft, ullmann);

            Dane dane = new Dane(
                new ArrayList<>(Arrays.asList(aho, hopcroft, ullmann)),
                new ArrayList<>(Arrays.asList(new Ksiazka("AiSD", aho, hopcroft, ullmann))),
                new ArrayList<>(Arrays.asList(bibl))
            );

            Serializacja.zapisz(dane, "dane.ser");
        }
    }
}