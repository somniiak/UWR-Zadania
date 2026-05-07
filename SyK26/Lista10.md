# Lista 10

### Zadanie 1
![](https://hackmd.io/_uploads/BJUmFsuCZg.png)

---

- Szerekość szyny adresowej: 12 bitów $\Rightarrow$ adresy od `000` do `FFF`
- Offset: 4 bajty bloku $\Rightarrow$ $\log_2 4$ = 2 bity
- Indeks: 4 zbiory $\Rightarrow$ $log_2 4$ = 2 bity
- Tag: pozostałe 12 - 2 - 2 = 8 bitów

<center>
    
| Bity 11 - 4       | Bity 3 – 2         | Bity 1 – 0          |
|-------------------|--------------------|---------------------|
| **tag** (8 bitów) | **index** (2 bity) | **offset** (2 bity) |

</center>

---

<center>

| Adres | Binarny                                                                                                                      | Trafienie? | Wartość |
|-------|------------------------------------------------------------------------------------------------------------------------------|------------|---------|
| `832` | $\underbrace{10000011}_{\text{tag} = 83} \quad \underbrace{00}_{\text{index} = 0} \quad \underbrace{10}_{\text{offset} = 2}$ | HIT        | `CC`    |
| `835` | $\underbrace{10000011}_{\text{tag} = 83} \quad \underbrace{01}_{\text{index} = 1} \quad \underbrace{01}_{\text{offset} = 1}$ | MISS       |         |
| `FFD` | $\underbrace{11111111}_{\text{tag} = FF} \quad \underbrace{11}_{\text{index} = 3} \quad \underbrace{01}_{\text{offset} = 1}$ | HIT        | `C0`    |

</center>

### Zadanie 2
![](https://hackmd.io/_uploads/rJt7YsuRWg.png)

---

![](https://hackmd.io/_uploads/BJuSw8Y0be.png)

**Pamięć podreczna z mapowaniem bezpośrednim adresowana bajtowo** - pamięć cache, w której każdy blok pamięci głównej jest przypisywany do dokładnie jednego wiersza w pamięci podręcznej. Wybór konkretnego wiersza w pamięci podręcznej jest dokonywany na podstawie adresu pamięci głównej.

Adres pamięci głównej jest dzielony na trzy części:
- *tag* - identyfikator bloku z pamięci
- *indeks* (wiersza) - do której linii cache'u trafi blok
- *offset* - który bajt wewnątrz bloku

---

- Rozmiar bloku w 32-bitowych słowach:
  $$B = 2^b = 2^5 = 32$$
- Liczba wierszy:
  Wierszy jest jest tyle co indeksów, a indeks ma 5 bitów:
  $$S = 2^S = 2^5 = 32$$
- Stosunek bitów danych do bitów metadanych:
  Bity danych na wiersz: $32 \text{ bajty } = 32 \times 8 = 256 \text{ bitów }$
  Bity metadanych (*tag* + *valid bit*):
    - tag $\equiv \text{addr}_{31\dots10}$ - 22 bity
    - valid - 1 bit
  $$\frac{\text{bity danych}}{\text{bity metadanych}} = \frac{256}{23} \approx 11,13$$

### Zadanie 3
![](https://hackmd.io/_uploads/rkpXKouCbe.png)

---

- **Trafienie**
Sytuacja, gdy procesor szuka bloku w cache i znajduje go tam (valid=1 i tag się zgadza). Dane są zwracane bezpośrednio z cache - szybko, bez odwoływania się do pamięci głównej.

- **Zastąpienie bloku**
Sytuacja, gdy blok danych musi zostać przeniesiony do pamięci podręcznej, a konkretny wiersz (wyznaczony przez index) jest zajęty (nawet jeśli reszta cache jest pusta).

- **Chybienie** (ang. *miss*)
Sytuacja, gdy procesor szuka bloku w cache ale nie znajduje go tam (brak wpisu, valid=0, lub tag się nie zgadza). Konieczne jest wtedy pobranie bloku z pamięci głównej (lub niższego poziomu hierarchii), co jest znacznie wolniejsze.

- **Chybienie przymusowe** (ang. *compulsory miss*)
Chybienie, które zawsze musi wystąpić przy pierwszym odwołaniu do danego bloku - cache na początku jest pusty i blok nie jest jeszcze obecny w pamięci podręcznej.

- **Chybienie z konfliktem** (ang. *conflict miss*)
Chybienie, które występuje wtedy, gdy dwa różne bloki mają ten sam indeks.

---

**(tag, index, offset) = (addr$_{31\dots10}$, addr$_{9\dots5}$, addr$_{4\dots0}$)**

- **Tag**: 22 bity
- **Indeks**: 5 bitów ($\Rightarrow$ **32 wiersze**)
- **Offset**: 5 bitów ($\Rightarrow$ **8 słow 32-bitowych**)

---

Adresy:
$$ 0, 4, 16, 132, 232, 160, 1024, 28, 140, 3100, 180, 2180 $$

</br>
<center>

| Adres | Tag             | Index       | Offset       | Trafienie | Typ          |
|-------|-----------------|-------------|--------------|-----------|--------------|
| 0     | `0...00000` = 0 | `00000` = 0 | `00000` = 0  | Miss      | compulsory   |
| 4     | `0...00000` = 0 | `00000` = 0 | `00100` = 4  | **Hit**   | -            |
| 16    | `0...00000` = 0 | `00000` = 0 | `10000` = 16 | **Hit**   | -            |
| 132   | `0...00000` = 0 | `00100` = 4 | `00100` = 4  | Miss      | compulsory   |
| 232   | `0...00000` = 0 | `00111` = 7 | `01000` = 8  | Miss      | compulsory   |
| 160   | `0...00000` = 0 | `00101` = 5 | `00000` = 0  | Miss      | compulsory   |
| 1024  | `0...00001` = 1 | `00000` = 0 | `00000` = 0  | Miss      | **conflict** |
| 28    | `0...00000` = 0 | `00000` = 0 | `11100` = 28 | Miss      | **conflict** |
| 140   | `0...00000` = 0 | `00100` = 4 | `01100` = 12 | **Hit**   | -            |
| 3100  | `0...00011` = 3 | `00000` = 0 | `11100` = 28 | Miss      | **conflict** |
| 180   | `0...00000` = 0 | `00101` = 5 | `10100` = 20 | **Hit**   | -            |
| 2180  | `0...00010` = 4 | `00100` = 4 | `00100` = 4  | Miss      | **conflict** |

</center>

---

**Liczba zastąpionych bloków**
Zastąpienie zachodzi tylko przy conflict miss na już zajętym wierszu: 4.

**Zawartość cache po wykonaniu odwołań (tag, index, offset_słów_w_bloku)**:
- **(3, 0, ..)** — blok załadowany przez adres 3100, wyparł blok z adresu 28
- **(4, 4, ..)** — blok załadowany przez adres 2180, wyparł blok z adresu 132/140
- **(0, 5, ..)** — blok załadowany przez adres 160, trafiony przez 180
- **(0, 7, ..)** — blok załadowany przez adres 232

Wiersze 1, 2, 3, 6, 8–31 są puste, bo nie było do nich żadnych odwołań.

**Efektywność pamięci podręcznej**
$$ \text{hit rate} = \frac{\text{4 trafienia}}{\text{12 odwołań}} \approx 33.33\% $$

### Zadanie 4
![](https://hackmd.io/_uploads/Hkb4KjdR-l.png)

### Zadanie 5
![](https://hackmd.io/_uploads/ryBNKoOAZl.png)

### Zadanie 6
![](https://hackmd.io/_uploads/r1C8YouCZg.png)

---

- Czas dostępu do pamięci głównej: **70 ns**
- Dostępy do pamięci: **36%** wszystkich instrukcji
- **L1**: rozmiar 2 KiB, wspł. chybień = 8.0%, czas dostępu = 0.66 ns (1 cykl)
- **L2**: rozmiar 1 MiB, wspł. chybień = 0.5%, czas dostępu = 5.62 ns
- CPI bazowe (bez dostępów do pamięci) = **1.0**

---

**Średni czas dostępu (tylko L1)**
- Zawsze czekamy 0.66 ns
- W 8% przypadków dodatkowo czekamy 70 ns

$$\text{AMAT}_{L1} = t_{L1} + \text{miss rate}_{L1} \cdot t_{mem}$$

$$\text{AMAT}_{L1} = 0.66 + 0.08 \cdot 70 = 0.66 + 5.6 = \textbf{6.26 ns}$$

**Średni czas dostępu (L1 + L2)**
- Zawsze czekamy 0.66 ns (L1)
- W 8% idziemy do L2 (5.62 ns)
- W 0.5% tych 8% idziemy do RAM (70 ns)

$$
\begin{aligned}
    \text{AMAT}_{L1+L2} &= t_{L1} + \text{miss rate}_{L1} \cdot (t_{L2} + \text{miss rate}_{L2} \cdot t_{mem}) \\
    &= 0.66 + 0.08 \cdot (5.62 + 0.005 \cdot 70) \\
    &= 0.66 + 0.08 \cdot (5.62 + 0.35) \\
    &= 0.66 + 0.08 \cdot 5.97 \\
    &= 0.66 + 0.4776 = \textbf{1.1376 ns}
\end{aligned}
$$

---

Kara za dostęp do pamięci doliczana jest tylko dla 36% instrukcji:

$$\text{CPI} = \text{CPI}_{base} + 0.36 \cdot \text{penalty}$$

gdzie **penalty** to dodatkowy czas oczekiwania (ponad czas L1) przeliczony na cykle (1 cykl = 0.66 ns).

### Tylko L1

$$\text{penalty}_{L1} = \text{miss rate}_{L1} \cdot \frac{t_{mem}}{t_{cyklu}} = 0.08 \cdot \frac{70}{0.66} = 0.08 \cdot 106.06 = 8.485 \text{ cykli}$$

$$\text{CPI}_{L1} = 1.0 + 0.36 \cdot 8.485 = 1.0 + 3.055 = \textbf{4.055}$$

### L1 + L2

$$
\begin{aligned}
\text{penalty}_{L1+L2} &= \text{miss rate}_{L1} \cdot \left(\frac{t_{L2}}{t_{cyklu}} + \text{miss rate}_{L2} \cdot \frac{t_{mem}}{t_{cyklu}}\right) \\
&= 0.08 \cdot \left(\frac{5.62}{0.66} + 0.005 \cdot \frac{70}{0.66}\right) \\
&= 0.08 \cdot (8.515 + 0.530) \\
&= 0.08 \cdot 9.045 = 0.7236 \text{ cykli}
\end{aligned}
$$

$$\text{CPI}_{L1+L2} = 1.0 + 0.36 \cdot 0.7236 = 1.0 + 0.2605 = \textbf{1.2605}$$

**Podsumowanie**
| Konfiguracja | AMAT    | CPI   |
|--------------|---------|-------|
| L1           | 6.26 ns | 4.055 |
| L1 + L2      | 1.14 ns | 1.261 |

Dodanie L2 drastycznie redukuje zarówno średni czas dostępu, jak i CPI — z $\space\approx$ 4 do 1,26.

### Zadanie 7
![](https://hackmd.io/_uploads/ryp4KsdAZe.png)
