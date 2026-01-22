package kosmos;

public enum Zodiak {
    BARAN(Energia.MESKA, Krzyz.KARDYNALNY, Zywiol.OGIEN),
    BYK(Energia.ZENSKA, Krzyz.STALY, Zywiol.ZIEMIA),
    BLIZNIETA(Energia.MESKA, Krzyz.ZMIENNY, Zywiol.POWIETRZE),
    RAK(Energia.ZENSKA, Krzyz.KARDYNALNY, Zywiol.WODA),
    LEW(Energia.MESKA, Krzyz.STALY, Zywiol.OGIEN),
    PANNA(Energia.ZENSKA, Krzyz.ZMIENNY, Zywiol.ZIEMIA),
    WAGA(Energia.MESKA, Krzyz.KARDYNALNY, Zywiol.POWIETRZE),
    SKORPION(Energia.ZENSKA, Krzyz.STALY, Zywiol.WODA),
    STRZELEC(Energia.MESKA, Krzyz.ZMIENNY, Zywiol.OGIEN),
    KOZIOROZEC(Energia.ZENSKA, Krzyz.KARDYNALNY, Zywiol.ZIEMIA),
    WODNIK(Energia.MESKA, Krzyz.STALY, Zywiol.POWIETRZE),
    RYBY(Energia.ZENSKA, Krzyz.ZMIENNY, Zywiol.WODA);

    public enum Energia {
        MESKA,
        ZENSKA;
    }

    public enum Krzyz {
        KARDYNALNY,
        STALY,
        ZMIENNY;
    }

    public enum Zywiol {
        OGIEN,
        ZIEMIA,
        POWIETRZE,
        WODA;
    }

    private final Energia energia;
    private final Krzyz krzyz;
    private final Zywiol zywiol;

    Zodiak(Energia energia, Krzyz krzyz, Zywiol zywiol) {
        this.energia = energia;
        this.krzyz = krzyz;
        this.zywiol = zywiol;
    }

    public Energia getEnergia() {
        return energia;
    }

    public Krzyz getKrzyz() {
        return krzyz;
    }

    public Zywiol getZywiol() {
        return zywiol;
    }
}
