# Lista 9

### Zadanie 1
![](https://hackmd.io/_uploads/BkRMrxlAZx.png)

### Zadanie 2
![](https://hackmd.io/_uploads/By7mSllA-x.png)

**Branch-target buffer** to mała pamięć podręczna przechowująca przewidywany adres następnej instrukcji po skoku. Struktura wpisu:

- adres instrukcji skoku (kolumna 1) – służy do dopasowania
- przewidywany PC (kolumna 2) – adres docelowy skoku
- opcjonalne bity stanu (kolumna 3) – dodatkowe informacje o predykcji

W BTB przechowuje się tylko skoki przewidywane jako wzięte – skok niewzięty po prostu pobiera kolejną instrukcję sekwencyjną, więc nie wymaga wpisu.

![](https://hackmd.io/_uploads/B18W_de0-l.png)

---

![](https://hackmd.io/_uploads/S1rUhdxAZl.png)

Rysunek pokazuje kroki wykonywane podczas używania BTB w prostym 5-fazowym potoku. Jak widać na tym rysunku, nie będzie żadnego opóźnienia skoku, jeśli wpis predykcji zostanie znaleziony w buforze i predykcja okaże się poprawna. W przeciwnym razie kara wyniesie co najmniej dwa cykle zegarowe. Obsługa błędnych predykcji i chybień jest poważnym wyzwaniem, ponieważ zazwyczaj trzeba wstrzymać pobieranie instrukcji na czas przepisania wpisu w buforze.

![](https://hackmd.io/_uploads/BJbKCOl0-l.png)

---

#### Predyktor 2-bitowy

Predyktor **1-bitowy** ma wadę: nawet jeśli skok jest prawie zawsze wzięty, po jednym wyjątku predyktor się myli dwa razy zamiast raz (bo bit zostaje odwrócony).

Predyktor **2-bitowy** rozwiązuje ten problem - predykcja zmienia się dopiero po dwóch kolejnych błędach. Mamy 4 stany:

- `11` - wzięty
- `10` - wzięty
- `01` - nie wzięty
- `00` - nie wzięty

Gdzie przechowywać bity predyktora 2-bitowego:

- jako mały cache indeksowany dolnymi bitami PC instrukcji skoku, dostępny w fazie IF
- jako bity dołączone do każdego bloku w cache instrukcji, pobierane razem z instrukcją

Przykład programu, dla którego 2-bitowy predyktor działa lepiej niż statyczny:
```c
for (int i = 0; i < 100; i++) { ... }
```

Predyktor statyczny np. zawsze przewiduje "nie wzięty" - myli się 99 razy na 101 iteracji. Predyktor 2-bitowy po pierwszych kilku iteracjach ustabilizuje się na stanie „silnie wzięty" i pomyli się tylko 2 razy (na początku i na końcu pętli).

Predyktor 2-bitowy możemy uogólnić do $n$-bitowego stosując licznik z zakresu od $0$ do $2^n - 1$. Wtedy jeśli wartość $\geq 2^{n - 1}$, przewidujemy skok.


### Zadanie 3
![](https://hackmd.io/_uploads/rJPmSggCbg.png)

Predyktor 2-bitowy z Appendix C patrzy wyłącznie na historię jednej gałęzi - nie uwzględnia zachowania innych skoków. W niektórych przypadkach wynik skoku zależy jednak od tego, co zrobiły poprzednie skoki, i lokalny predyktor nigdy tego nie uuchwyci. Predykatory korelujące mają wychwycić te zależności.

---

#### Przykład kodu, dla którego lokalny predyktor zawodzi

Z benchmarku `eqntott`:

```c
if (aa == 2)
        aa = 0;

if (bb == 2)
        bb = 0;

if (aa != bb)
        { ... }
```

Kluczowa obserwacja: jeśli ani pierwszy, ani drugi skok nie są wzięte (czyli `aa=0` i `bb=0`), to ostatni na pewno nie zostanie wzięty (`aa == bb`). Wynik ostatniego skoku jest więc w pełni zależny b1 i b2 - a lokalny predyktor patrzący tylko na historię ostatniego skoku tego nie wykryje.

---

#### Ogólna struktura predyktorów korelujących

Predyktor **$(m, n)$** używa historii **$m$ ostatnich skoków** do wyboru spośród $2^m$ predyktorów $n$-bitowych dla danej gałęzi.

- Historia m ostatnich skoków przechowywana jest w **m-bitowym rejestrze przesuwnym** (1 = taken, 0 = not taken).
- Indeks do tablicy predyktorów tworzy się przez konkatenację dolnych bitów adresu skoku z m-bitową historią globalną.
- Liczba bitów w predyktorze $(m,n)$: $2^m \times n \times \text{Liczba wpisów wybranych adresem}$

$2$-bitowy predyktor bez globalnej historii jest po prostu $(0,2)$-predyktorem.

Przykład: predyktor **(2,2)** z 1K wpisami ma tyle samo bitów co standardowy **(0,2)** z 4K wpisami (`4 × 2 × 1K = 8K bitów`), a osiąga **lepszą dokładność** – często nawet lepszą niż (0,2) z nieskończoną liczbą wpisów.

---

#### Predyktor gshare

W predyktorze **gshare** indeks tworzony jest przez połączenie **adresu skoku** oraz **wyników ostatnich skoków warunkowych** za pomocą operacji **XOR**, która działa jak funkcja haszująca adres skoku i historię skoków. Wynik haszowania służy do indeksowania **tablicy 2-bitowych liczników** predykcji.

![](https://hackmd.io/_uploads/BJTn6VgCWe.png)


### Zadanie 4
![](https://hackmd.io/_uploads/r1i7HgxCWg.png)

#### Czym są predyktory turniejowe

Predyktory turniejowe używają wielu predyktorów jednocześnie, zazwyczaj globalnego i lokalnego, i dynamicznie **wybierają między nimi** za pomocą selektora.

**Predyktor globalny** – indeksuje tablicę predykcji za pomocą historii ostatnich skoków (niezależnie od adresu bieżącego skoku).

**Predyktor lokalny** – indeksuje tablicę predykcji za pomocą adresu bieżącego skoku.

Predyktor turniejowy potrafi dobrać właściwy predyktor dla konkretnej gałęzi

---

#### Jak działa selektor?

Selektor działa jak predyktor 2-bitowy, zmieniając preferowany predyktor dla danego adresu skoku, gdy wystąpią **dwie błędne predykcje z rzędu**. Warto zauważyć, że obsługa błędnej predykcji jest nieco skomplikowana, ponieważ trzeba zaktualizować zarówno **tablicę selektora**, jak i **predyktor globalny lub lokalny** (w zależności od tego, który był wybrany).

![](https://hackmd.io/_uploads/S1jg1Sx0Wg.png)


### Zadanie 5
![](https://hackmd.io/_uploads/ByRmBleRZx.png)

![](https://hackmd.io/_uploads/Bk2w6FgA-l.png)

**Predyktor TAGE (TAgged GEometric)**

Pięciokomponentowy predyktor tagged hybrid posiada pięć osobnych tablic predykcji, indeksowanych hashem adresu skoku i fragmentem niedawnej historii skoków o długości od 0 do 4, oznaczonej jako "h" na rysunku. Hash może być tak prosty jak operacja XOR, jak w predyktorze gshare. Każdy predyktor jest predyktorem 2-bitowym (lub ewentualnie 3-bitowym). Tagi mają typowo **4–8 bitów**. Wybierana predykcja to ta pochodząca z tablicy o **najdłuższej historii**, dla której tagi również pasują.

---

#### Struktura predyktora TAGE

Predyktor składa się z **n+1 tablic predykcji**: P(0), P(1), ..., P(n).

**P(0) – predyktor bazowy:**
- indeksowany wyłącznie **adresem skoku** (bez historii)
- nie używa tagów
- zawsze daje dopasowanie – jest **domyślną predykcją** gdy żadna z pozostałych tablic nie pasuje

**P(1) ... P(n) – predyktory z historią:**
- każda tablica P(i) jest indeksowana **hashem** (np. XOR) adresu skoku i **historii ostatnich i skoków** o długości L(i)
- długości historii są **geometrycznie rosnące**: L(1) < L(2) < ... < L(n)
- każdy wpis zawiera:
  - **predykcję** – licznik 2-bitowy (lub 3-bitowy, co daje nieco lepsze wyniki)
  - **tag** – krótki, typowo **4–8 bitów**, służy do weryfikacji dopasowania
  - **pole użycia (use field)** – 2-bitowy licznik wskazujący czy predykcja była niedawno używana; okresowo resetowany, by usuwać stare wpisy

---

#### Zasada działania

1. Wszystkie tablice P(0)...P(n) są odpytywane **równolegle**.
2. W tablicach P(1)...P(n) sprawdzane jest **dopasowanie tagu** – tag wpisu musi zgadzać się z hashem adresu skoku i historii.
3. Wybierana jest predykcja z tablicy o **najdłuższej historii**, której tag pasuje.
4. Jeśli żaden tag nie pasuje → używana jest predykcja z **P(0)**.
