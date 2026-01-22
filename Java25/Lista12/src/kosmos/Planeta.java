package kosmos;

public enum Planeta {
    MERKURY(330.2e21, 4879, 57909170., 88, "szary", TypPlanety.SKALISTA),
    WENUS(4868.5e21, 12104, 108208926., 225, "biały", TypPlanety.SKALISTA),
    ZIEMIA(5974.2e21, 12756, 149597887., 365, "niebieski", TypPlanety.SKALISTA),
    MARS(641.9e21, 6805, 227936637., 687, "pomarańczowy", TypPlanety.SKALISTA),
    JOWISZ(1898600.8e21, 142984, 778412027., 4333, "beżowy", TypPlanety.GAZOWA),
    SATURN(568516.8e21, 120536, 1426725413., 10759, "kremowy", TypPlanety.GAZOWA),
    URAN(86841e21, 51118, 2870972220., 30685, "biały", TypPlanety.GAZOWO_LODOWA),
    NEPTUN(102439.6e21, 49528, 4498252900., 60189, "jasnoniebieski", TypPlanety.GAZOWO_LODOWA);

    public enum TypPlanety {
        SKALISTA,
        GAZOWA,
        GAZOWO_LODOWA;
    }

    private final double masa;
    private final int srednica;
    private final double odlegloscOdSlonca;
    private final int okresOrbitalny;
    private final String kolor;
    private final TypPlanety typ;

    Planeta(double masa, int srednica, double odlegloscOdSlonca, int okresOrbitalny, String kolor, TypPlanety typ) {
        this.masa = masa;
        this.srednica = srednica;
        this.odlegloscOdSlonca = odlegloscOdSlonca;
        this.okresOrbitalny = okresOrbitalny;
        this.kolor = kolor;
        this.typ = typ;
    }

    public double getMasa() {
        return masa;
    }

    public int getSrednica() {
        return srednica;
    }

    public double getOdlegloscOdSlonca() {
        return odlegloscOdSlonca;
    }

    public int getOkresOrbitalny() {
        return okresOrbitalny;
    }

    public String getKolor() {
        return kolor;
    }

    public TypPlanety getTyp() {
        return typ;
    }
}
