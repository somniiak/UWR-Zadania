# Lista 11

# Zadanie 1
![](https://hackmd.io/_uploads/SJ5mJ8zyfl.png)

**a)**
- 512B - pamięć podręczna
- Mapowanie bezpośrednie (*direct mapping*)
- 16B - rozmiar bloku

* Liczba bloków: $512 / 16 = 32$
* Bity offsetu: $\log_2{16} = 4$
* Bity indeksu: $\log_2{32} = 5$

Wiersz `x[0][i]` ma adres `4i`, wiersz `x[1][i]` ma adres `512 + 4i`.
Różnica 512B (rozmiar pamięci podręcznej) - oba wiersze mapują się na te same zestawy.

Każda iteracja:
- `x[0][i]`: czyta z zestawu S. Jeśli zimny miss → ładuje blok (4 inty). Miss.
- `x[1][i]`: mapuje na ten sam zestaw co `x[0][i]`. Wypiera go. Miss.
W kolejnej iteracji `x[0][i+1]` może trafić w załadowany blok (co 4 inty) – ale tylko jeśli nie zostało wypchnięte.

Ponieważ oba wiersze kolidują, każdy dostęp do `x[1][i]` wypiera blok `x[0][...]`, a przy kolejnym dostępie do `x[0][...]` blok też jest nieaktualny. Co 4 iteracje ładujemy nowy blok `x[0][...]` i nowy blok `x[1][...]`.

Miss: **100%**

**b)**
- 1024B - pamięć podręczna
- Mapowanie bezpośrednie (*direct mapping*)
- 16B - rozmiar bloku

* Liczba bloków: $1024 / 16 = 64$
* Bity offsetu: $\log_2{16} = 4$
* Bity indeksu: $\log_2{64} = 6$

Teraz pamięć podręczna ma 1024B, a odległość między `x[0]` i `x[1]` wynosi 512B - nie kolidują (mieszczą się jednocześnie). Każdy blok (16B = 4 inty) ładowany jest raz przy pierwszym dostępie, a pozostałe 3 dostępy to trafienia.

Dla każdego z 2 wierszy * 32 bloków = 64 bloków -> 64 missy cold-start.

Miss: $64 / 256$ = **25%**

**c) 512B, dwudrożna, sekwencyjno-skojarzeniowa, zastępowanie LRU, blok 16B**
- 512B - pamięć podręczna
- Dwudrożna sekcyjno-skojarzeniowa (*2-way set associative*)
- Zastępowanie LRU
- 16B - rozmiar bloku

* Liczba zestawów: $512 / (2 \times 16) = 16$ zestawów
* Każdy zestaw ma 2 drogi (LRU)

Adres `x[0][i]` = `4i`, adres `x[1][i]` = `512 + 4i`. Numer zestawu zależy od bitów adresu (4 bity = 16 zestawów).
Różnica adresów = 512 → bity 4–7 dla `x[0][i]` i `x[1][i]` są takie same - kolidują w tym samym zestawie. Ale teraz mamy 2 drogi, czyli oba bloki mieszczą się jednocześnie w zestawie.

Przebieg dla jednego zestawu (4 kolejne elementy z obu wierszy):
- `x[0][4k]`: **miss** (cold), ładuje blok do drogi 0
- `x[1][4k]`: **miss** (cold), ładuje blok do drogi 1
- `x[0][4k+1]`: **trafienie** (blok nadal w drodze 0)
- `x[1][4k+1]`: **trafienie** (blok nadal w drodze 1)
- `x[0][4k+2]`: **trafienie**
- `x[1][4k+2]`: **trafienie**
- `x[0][4k+3]`: **trafienie**
- `x[1][4k+3]`: **trafienie**

Na 8 dostępów: 2 chybienia.
Łącznie: 128/4 * 2 wiersze = 64 chybienia, 256 dostępów.

Miss: $64 / 256$ = **25%**

# Zadanie 2
![](https://hackmd.io/_uploads/S1dLbUMJfx.png)


- `struct pixel` = 4 bajty (r, g, b, a)
- `buffer[480][640]` → wiersze po 640 × 4 = **2560 bajtów**
- Cache: 32 KB = 32768 bajtów, mapowanie bezpośrednie, blok **8 bajtów**
- Liczba linii: 32768 / 8 = **4096 linii**
- `buffer` pod adresem `0x0`, write-back write-allocate

Jeden piksel = 4 bajty, jeden blok = 8 bajtów -> 2 piksele na blok.

```
buffer[0][0], buffer[0][1], ..., buffer[0][639],
buffer[1][0], buffer[1][1], ..., buffer[1][639],
...
```

Sąsiednie elementy **tego samego wiersza** leżą obok siebie. Sąsiednie elementy **tej samej kolumny** są odległe od siebie o 2560 bajtów.

---

```c
for (j = 639; j >= 0; j--) {
    for (i = 479; i >= 0; i--) {
        buffer[i][j].r = 0;
        buffer[i][j].g = 0;
        buffer[i][j].b = 0;
        buffer[i][j].a = 0;
    }
}
```

Dla ustalonego `j`, kolejne iteracje po `i` sięgają po:
`buffer[479][j],  buffer[478][j],  buffer[477][j], ...`.
Każde przejście do `buffer[i-1][j]` to skok o **2560 bajtów** w pamięci.

Blok ma 8 bajtów = 2 piksele. Załadowanie `buffer[i][j]` ładuje też `buffer[i][j+1]` (sąsiad w tym samym wierszu) – ale pętla **nigdy do niego nie wraca** w tej samej iteracji po `j`. Sąsiad w bloku jest bezużyteczny.

Cztery dostępy `.r`, `.g`, `.b`, `.a` dotyczą tego samego piksela - tych samych 4 bajtów **tego samego bloku**. Więc:

- `.r` → **miss** (ładuje blok)
- `.g` → **hit** (ten sam blok, offset +1)
- `.b` → **hit** (offset +2)
- `.a` → **hit** (offset +3)

Na piksel: **1 miss + 3 hity**.
Miss: $1 / 4$ = 25% $\Rightarrow$ Hit: 75%.

# Zadanie 3
![](https://hackmd.io/_uploads/ryZ4kIf1fx.png)

**Wersja 1 (char\*):**
```c
char *cptr = (char *) buffer;
while (cptr < (((char *) buffer) + 640 * 480 * 4)) {
    *cptr = 0;
    cptr++;
}
```

**Wersja 2 (int\*):**
```c
int *iptr = (int *)buffer;
while (iptr < ((int *)buffer + 640*480)) {
    *iptr = 0;
    iptr++;
}
```

Wersja 1 zapisuje **1 bajt** na iterację, wersja 2 zapisuje **4 bajty** (cały piksel) na iterację. Obie przechodzą przez całą tablicę sekwencyjnie, w kolejności wierszowej.

Cache: 32 KB, mapowanie bezpośrednie, blok **8 bajtów**.

**Wersja 1 – zapis po 1 bajcie:**
- bajt 0 bloku -> miss, ładuje blok, zapis
- bajt 1 -> hit
- bajt 2 -> hit
- bajt 3 -> hit
- bajt 4 -> hit
- bajt 5 -> hit
- bajt 6 -> hit
- bajt 7 -> hit

Na każde 8 dostępów: **1 miss + 7 hitów**.
**trafienia** = 7/8 = 87,5%

**Wersja 2 – zapis po 4 bajty (int):**

- int 0 (bajty 0–3) -> miss, ładuje blok, zapis
- int 1 (bajty 4–7) -> hit

Na każde 2 dostępy: **1 miss + 1 hit**.
**trafienia** = 1/2 = 50,0%

Wersja 1: 640 × 480 × 4 = **1 228 800 dostępów**
Wersja 2: 640 × 480 = **307 200 dostępów**

Wersja 1 ma więcej trafień tylko dlatego, że ma więcej zbędnych dostępów do cache.

**Wersja 2 jest lepsza** – mniej pracy procesora, mniej iteracji pętli, taki sam ruch do RAM.


# Zadanie 4
![](https://hackmd.io/_uploads/BJBV1IzkGl.png)


Normalnie indeks zestawu bierzemy ze *środkowych* bitów adresu, a najstarsze bity idą na tag.

Weźmy cache z 4 zestawami (indeks = 2 bity) i blokiem 4 bajtów (offset = 2 bity), adresy 8-bitowe:
```
[ bity 7-4: tag ][ bity 3-2: indeks ][ bity 1-0: offset ]
```

Jeśli zamienimy tag z indeksem:
```
[ bity 7-6: indeks ][ bity 5-2: tag ][ bity 1-0: offset ]
```

Indeks zależy teraz od najstarszych bitów. Ale programy prawie zawsze działają w małym wycinku przestrzeni adresowej – tablice, zmienne lokalne, kod – wszystko leży blisko siebie, w tym samym obszarze pamięci. To oznacza, że najstarsze bity adresu są stale takie same dla wszystkich aktywnych danych.

Zamiast równomiernie rozkładać dane po wszystkich zestawach, pakujemy je do jednego. Cache o pojemności np. 1 KB zachowuje się jak cache o pojemności 1/4 KB – reszta jest zmarnowana. Współczynnik chybień rośnie dokładnie tak, jakbyśmy mieli dużo mniejszą pamięć podręczną.

Środkowe bity są dobre właśnie dlatego, że zmieniają się często nawet przy sekwencyjnych dostępach (każdy nowy blok to inny indeks), co gwarantuje równomierne wykorzystanie wszystkich zestawów.

# Zadanie 5
![](https://hackmd.io/_uploads/SyaHqWm1Gg.png)

Niech cache ma 2 linie:
- Bezpośrednia (1-drożna): 2 zestawy, każdy z 1 drogą
- Dwudrożna (LRU): 1 zestaw z 2 drogami

Niech bloki A, B, C mapują się wszystkie na ten sam zestaw w cache dwudrożnej (czyli mają ten sam indeks). W cache bezpośredniej A i C mapują na linię 0, B mapuje na linię 1.

```
A, B, C, A, B, C, A, B, C, ...
```

---

**Cache bezpośrednia**
| Dostęp | Linia 0 | Linia 1 | Wynik |
|--------|---------|---------|-------|
| A | **A** | - | miss |
| B | A | **B** | miss |
| C | **C** | B | miss (C wypycha A) |
| A | **A** | B | miss (A wypycha C) |
| B | A | **B** | hit (B nadal w linii 1) |
| C | **C** | B | miss |
| A | **A** | B | miss |
| B | A | **B** | hit |
| C | **C** | B | miss |

B nigdy nie jest wypychane, bo siedzi w innej linii niż A i C - A i C zawsze miss, B zawsze hit. **Współczynnik chybień = 66.67%**

---

**Cache dwudrożna z LRU**
Wszystkie trzy bloki walczą o jeden zestaw z 2 drogami:

| Dostęp | Droga 0 | Droga 1 | LRU | Wynik |
|--------|---------|---------|-----|-------|
| A | **A** | - | A | miss |
| B | A | **B** | A | miss |
| C | **C** | B | B | miss (C wypycha A – LRU) |
| A | C | **A** | C | miss (A wypycha B – LRU) |
| B | **B** | A | A | miss (B wypycha C – LRU) |
| C | B | **C** | B | miss (C wypycha A – LRU) |
| A | **A** | C | C | miss |
| B | A | **B** | ... | miss |
| C | ... | ... | ... | miss |

LRU zawsze wyrzuca dokładnie ten blok, który będzie potrzebny jako następny. Każdy dostęp to miss. **Współczynnik chybień = 100%**

Mamy 3 bloki konkurujące o 2 drogi. `A->B->C->A->B->C` sprawia, że najdawniej używany blok to zawsze ten, który właśnie zaraz będziemy potrzebować. W cache bezpośredniej A i C kolidują ze sobą, ale B siedzi w swojej linii.

# Zadanie 6
![](https://hackmd.io/_uploads/HyAge8fJMe.png)

# Zadanie 7
![](https://hackmd.io/_uploads/SkOWx8z1Gg.png)

# Zadanie 8
![](https://hackmd.io/_uploads/HkkzeUfkfl.png)
