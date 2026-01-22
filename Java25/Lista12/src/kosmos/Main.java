package kosmos;

import java.net.URL;
import java.util.EnumMap;
import java.util.EnumSet;

public class Main {
    private static void planety() throws Exception {
        EnumMap<Planeta, URL> obrazkiPlanet = new EnumMap<>(Planeta.class);

        obrazkiPlanet.put(Planeta.MERKURY,
                new URL("https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg"));

        obrazkiPlanet.put(Planeta.WENUS,
                new URL("https://upload.wikimedia.org/wikipedia/commons/c/c7/PIA23791-Venus-RealAndEnhancedContrastViews-20200608_%28cropped%29.jpg"));

        obrazkiPlanet.put(Planeta.ZIEMIA,
                new URL("https://upload.wikimedia.org/wikipedia/commons/c/cb/The_Blue_Marble_%28remastered%29.jpg"));

        obrazkiPlanet.put(Planeta.MARS,
                new URL("https://upload.wikimedia.org/wikipedia/commons/5/56/Mars_Valles_Marineris.jpeg"));

        obrazkiPlanet.put(Planeta.JOWISZ,
                new URL("https://upload.wikimedia.org/wikipedia/commons/0/0d/Jupiter_and_its_shrunken_Great_Red_Spot_%28cropped%29.jpg"));

        obrazkiPlanet.put(Planeta.SATURN,
                new URL("https://upload.wikimedia.org/wikipedia/commons/c/c1/Saturn_-_April_25_2016_%2837612580000%29.png"));

        obrazkiPlanet.put(Planeta.URAN,
                new URL("https://upload.wikimedia.org/wikipedia/commons/6/69/Uranus_Voyager2_color_calibrated.png"));

        obrazkiPlanet.put(Planeta.NEPTUN,
                new URL("https://upload.wikimedia.org/wikipedia/commons/6/61/Neptune_Voyager2_color_calibrated%2C_brightened.png"));

        obrazkiPlanet.entrySet().stream()
                .sorted((e1, e2) -> Double.compare(
                        e1.getKey().getOdlegloscOdSlonca(), e2.getKey().getOdlegloscOdSlonca()))
                .forEach(e -> {
                    System.out.println(
                            e.getKey().name() + " (" + e.getKey().getOdlegloscOdSlonca() + "km): " + e.getValue()
                    );
                });
    }

    private static void zodiak() {
        EnumSet<Zodiak> aktywne = EnumSet.noneOf(Zodiak.class);
        for (Zodiak z : Zodiak.values())
            if (z.getEnergia() == Zodiak.Energia.MESKA)
                aktywne.add(z);

        EnumSet<Zodiak> stale = EnumSet.noneOf(Zodiak.class);
        for (Zodiak z : Zodiak.values())
            if (z.getKrzyz() == Zodiak.Krzyz.STALY)
                stale.add(z);

        EnumSet<Zodiak> powietrzne = EnumSet.noneOf(Zodiak.class);
        for (Zodiak z : Zodiak.values())
            if (z.getZywiol() == Zodiak.Zywiol.POWIETRZE)
                powietrzne.add(z);

        EnumSet<Zodiak> suma = EnumSet.copyOf(aktywne);
        suma.addAll(stale);
        suma.addAll(powietrzne);

        EnumSet<Zodiak> przekroj = EnumSet.copyOf(aktywne);
        przekroj.retainAll(stale);
        przekroj.retainAll(powietrzne);

        System.out.println("Suma: " + suma);
        System.out.println("Przekrój: " + przekroj);
    }

    public static void main(String[] args) throws Exception {
        planety();
        zodiak();
    }
}