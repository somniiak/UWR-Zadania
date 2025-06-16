// Artur Dzido
// Lista 5
// (OpenJDK 21)

import java.util.ArrayList;

class Ksiazka{
    String tytul;
    ArrayList<Pisarz> autorzy = new ArrayList<Pisarz>();

    Ksiazka(String tytul, Pisarz... autorzy) {
        this.tytul = tytul;
        for (Pisarz p : autorzy) {
            this.autorzy.add(p);
        }
    }

    @Override public String toString() {
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

class Pisarz {
    String pseudonim;
    ArrayList<Obserwator> obserwatorzy = new ArrayList<Obserwator>();
    ArrayList<Ksiazka> ksiazki = new ArrayList<Ksiazka>();

    Pisarz (String pseudonim, Obserwator w)
    {
        this.pseudonim = pseudonim;
        this.obserwatorzy.add(w);
    }
    
    void napisz(String tytul) {
        napiszKsiazke(tytul, this); // Pisze sam
    }

    static void napiszKsiazke(String tytul, Pisarz... autorzy) {
        Ksiazka ksiazka = new Ksiazka(tytul, autorzy);
        for (Pisarz p : autorzy) {
            p.ksiazki.add(ksiazka);
            for (Obserwator o : p.obserwatorzy) {
                o.powiadomienie(ksiazka);
            }
        }
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

class Wydawnictwo implements Obserwator {
    char nazwa;

    Wydawnictwo(char nazwa) {
        this.nazwa = nazwa;
    }

    void wydajKsiazke(Ksiazka ksiazka) {
        System.out.println("Wydaje ksiazkę" + ksiazka);
    }

    public void powiadomienie(Ksiazka ksiazka) {
        if (ksiazka.tytul.charAt(0) == this.nazwa)
            this.wydajKsiazke(ksiazka);
    }

    @Override public String toString() {
        return Character.toString(nazwa);
    }
}

class Czytelnik implements Obserwator
{
    public void powiadomienie(Ksiazka ksiazka) {
        System.out.println("Nowa ksiazka " + ksiazka);
    }
}

class Recenzent implements Obserwator
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

class Biblioteka implements Obserwator
{
    String nazwa;

    Biblioteka(String nazwa) {
        this.nazwa = nazwa;
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

public class Literatura
{
    public static void main(String[] args) {
        Wydawnictwo a = new Wydawnictwo('T');
        Pisarz aho = new Pisarz("aho", a);
        Pisarz hopcroft = new Pisarz("hopcroft", a);
        Pisarz ullmann = new Pisarz("ullmann", a);
        Recenzent recz = new Recenzent("Gal_Anonim");
        Biblioteka bibl = new Biblioteka("BUWr");
        aho.dodajObserwatora(bibl);
        aho.dodajObserwatora(recz);
        Pisarz.napiszKsiazke("AiSD", aho, hopcroft, ullmann);
        System.out.println(aho.ksiazki.get(0).toString());
    }
}