# Lista 12

### Zadanie 1
![](https://hackmd.io/_uploads/SJIqRDsJGx.png)

---

**Translacja adresów** - proces tłumaczenia adresów wirtualnych na fizyczne.

**TLB (Translation lookaside buffer)** - pamieć pomocnicza do obługi pamięci wirtualnej (działa jak cache dla MMU).

**Tablica stron** - pamięć przechowująca informacje o adresach fizycznych poprzednio wczytanych do pamięci operacyjnej lub jeszcze znajdujących się na dysku.

---

**Adres wirutalny**:
- **TLBI (TLB index)** - indeks zbioru w TLB
- **TLBT (TLB tag)** - tag bloku w TLB
- **VPO (Virtual Page Offset)** - przesunięcie strony w pamięci wirtualnej
- **VPN (Virtual Page Number)** - numer strony w pamięci wirtualnej (pokrywa się z TLBI oraz TLBT)

**Adresu fizyczny**:
- **CT (Cache Tag)**
- **CI (Cache Index)**
- **CO (Cache Offset)**
- **PPN (Physical Page Number)** - numer strony w pamięci fizycznej
- **PPO (Physical Page Offset)**- przesunięcie strony w pamięci fizycznej (jest takie same jak VPO)

---

**Translacja adresu**:
1. Sprawdzamy, czy **TLBI** oraz **TLBT** są w **TLB** oraz czy są Valid.
2. Jeżeli tak => odczytujemy **PPN** z **TLB**.
3. Jeżeli nie => szukamy **PPN** w tablicy stron za pomoca **VPN**.
4. przepisujemy **VPO** do **PPO**.
5. Odczytujemy **CT**, **CI**, **CO**.

---

**Adres 1** (0x027c):
`0x027c`$_{(16)}$ = `00 0010 0111 1100`$_{(2)}$

```
TLBT = 000010   = 0x02
TLBI = 01       = 0x01
VPN  = 00001001 = 0x09
VPO  = 111100   = 0x3c
```

Wartość w TLB nie jest Valid, wiec szukamy za pomoca VPN.

```
PPN = 0x17 = 010111
PPO = 0x3c = 111100
```

Adres po translacji:  `0101 1111 1100`

```
CT = 0101111 = 0x17
CI = 1111    = 0x0f
CO = 00      = 0x00
```

**Adres 2** (0x03a9):
`0x03a9`$_{(16)}$ = `00 0011 1010 1001`$_{(2)}$

```
TLBT = 000011   = 0x03
TLBI = 10       = 0x02
VPN  = 00001110 = 0x0e
VPO  = 101001   = 0x29
```

Wartość w TLB nie jest Valid, wiec szukamy za pomoca VPN.

```
PPN = 0x11 = 00010001
PPO = 0x3c = 101001
```

Adres po translacji:  `0100 0110 1001`

```
CT = 010001  = 0x11
CI = 1010    = 0x0a
CO = 01      = 0x01
```

**Adres 3** (0x0040):

`0x0040`$_{(16)}$ = `00 0000 0100 0000`$_{(2)}$

```
TLBT = 000000   = 0x00
TLBI = 01       = 0x01
VPN  = 00000001 = 0x01
VPO  = 000000   = 0x00
```

Nie ma tego tagu w TLB, więc szukamy za pomocą VPN.
Pod ustalonym VPN nie ma wartości w tablicy stron, więc mamy chybienie.


### Zadanie 2
![](https://hackmd.io/_uploads/ryN21uiyGl.png)

---

**TLB w pełni asocjacyjna** – każdy adres może zostać zapamiętany w dowolnym bloku pamięci podręcznej, brak indeksów.

**Wtoczenie** – wczytanie wpisu w tablicy stron, którego nie było w pamięci głównej.

**Ramka** – fragment pamięci fizycznej.

**Błąd strony** – rodzaj błędu kiedy uruchomiony program uzyskuje dostęp do strony pamięci, która nie jest obecnie mapowana do wirtualnej przestrzeni adresowej procesu.

---

Adres: **4669** = `0001 0010 0011 1101` => Tag: 1
- Szukamy VPN=1 w TLB -> nie ma. Chybienie TLB.
- Szukamy VPN=1 w tablicy stron -> Valid=0, strona na dysku. Błąd strony (page fault).
- Swap-in: ładujemy stronę 1 z dysku do nowej ramki. Największy PPN = 12, więc nowa ramka: PPN=13.
- Aktualizujemy tablicę stron: VPN=1 → PPN=13, Valid=1.
- Wstawiamy do TLB (wyrzucamy LRU=3, czyli wpis z VPN=4).

| Valid | VPN | LRU | PPN |
|-------|-----|-----|-----|
| 1 | 11 | 1 | 12 |
| 1 | 7 | 2 | 4 |
| 1 | 3 | 3 | 6 |
| 1 | **1** | **0** | **13** |

Adres: **2227** = `0000 1000 1011 0011` => Tag: 0
- Szukamy VPN=0 w TLB -> nie ma. Chybienie TLB.
- Szukamy VPN=0 w tablicy stron -> Valid=1, PPN=5. Trafienie w tablicę stron.
- Wstawiamy do TLB (wyrzucamy LRU=3, czyli VPN=3).

| Valid | VPN | LRU | PPN |
|-------|-----|-----|-----|
| 1 | 1 | 1 | 13 |
| 1 | 11 | 2 | 12 |
| 1 | 7 | 3 | 4 |
| 1 | **0** | **0** | **5** |

Adres: **13916** = `0011 0110 0101 1100` => Tag: 3
- Szukamy VPN=3 w TLB -> nie ma. Chybienie TLB.
- Szukamy VPN=3 w tablicy stron -> Valid=1, PPN=6. Trafienie w tablicę stron.
- Wstawiamy do TLB (wyrzucamy LRU=3, czyli VPN=7).

| Valid | VPN | LRU | PPN |
|-------|-----|-----|-----|
| 1 | 0 | 1 | 5 |
| 1 | 1 | 2 | 13 |
| 1 | 11 | 3 | 12 |
| 1 | **3** | **0** | **6** |

Adres: **34587** = `1000 0111 0001 1011` => Tag: 8
- Szukamy VPN=8 w TLB -> nie ma. Chybienie TLB.
- Szukamy VPN=8 w tablicy stron -> Valid=0, strona na dysku. Błąd strony.
- Nowa ramka: PPN=14 (poprzedni max był 13).
- Aktualizujemy tablicę stron: VPN=8 -> PPN=14, Valid=1.
- Wstawiamy do TLB (wyrzucamy LRU=3, czyli VPN=11).

| Valid | VPN | LRU | PPN |
|-------|-----|-----|-----|
| 1 | 3 | 1 | 6 |
| 1 | 0 | 2 | 5 |
| 1 | 1 | 3 | 13 |
| 1 | **8** | **0** | **14** |

Adres: **48870** = `1011 1110 1110 0110` => Tag: 11
- Szukam VPN=11 w TLB -> nie ma. Chybienie TLB.
- Szukam VPN=11 w tablicy stron -> Valid=1, PPN=12. Trafienie w tablicę stron.
- Wstawiamy do TLB (wyrzucamy LRU=3, czyli VPN=1).

| Valid | VPN | LRU | PPN |
|-------|-----|-----|-----|
| 1 | 8 | 1 | 14 |
| 1 | 3 | 2 | 6 |
| 1 | 0 | 3 | 5 |
| 1 | **11** | **0** | **12** |

Adres: **12608** = `0011 0001 0100 0000` => Tag: 3
- Szukamy VPN=3 w TLB -> znaleziony. PPN=6, Valid=1. Trafienie TLB.
- Aktualizujemy LRU (VPN=3 staje się najświeższy).

| Valid | VPN | LRU | PPN |
|-------|-----|-----|-----|
| 1 | 11 | 1 | 12 |
| 1 | 8 | 2 | 14 |
| 1 | 0 | 3 | 5 |
| 1 | **3** | **0** | **6** |

Adres: **49225** = `1100 0000 0100 1001` => Tag: 12
- Szukamy VPN=12 w TLB -> nie ma. Chybienie TLB.
- Szukamy VPN=12 w tablicy stron -> Valid=0, brak (nie ma na dysku). Błąd strony.
- Nowa ramka: PPN=15.
- Aktualizujemy tablicę stron: VPN=12 -> PPN=15, Valid=1.
- Wstawiamy do TLB (wyrzucamy LRU=3, czyli VPN=0).

| Valid | VPN | LRU | PPN |
|-------|-----|-----|-----|
| 1 | 3 | 1 | 6 |
| 1 | 11 | 2 | 12 |
| 1 | 8 | 3 | 14 |
| 1 | **12** | **0** | **15** |

**Zmiany w tablicy stron**
| VPN | Valid | PPN | Zmiana |
|-----|-----|-------|--------|
| 1 | 1 | 13 | swap-in (dostęp 1) |
| 8 | 1 | 14 | swap-in (dostęp 4) |
| 12 | 1 | 15 | nowa ramka (dostęp 7) |


### Zadanie 3
![](https://hackmd.io/_uploads/BkGi0Ps1Mx.png)

---

**a) Jednopoziomowa tablica stron**

- 32-bitowe adresy wirtualne
  => $2^{32}$ możliwych adresów
- Rozmiar strony: 4KiB
  => $4 \cdot 2^{10}$ bajtów = $2^{12}$ bajtów

Liczba stron: $2^{32} / 2^{12} = 2^{20}$ = 1 048 576

- Rozmiar wpisu tablicy stron: 4 bajty 

Rozmiar całej tablicy: $2^{20} \times 4 = 2^{22}$ bajtów = 4MiB

**b) Dwupoziomowa tablica stron**

- Tablica stron pierwszego poziomu: 1024 wpisy
  => 1024 wpisy $\times$ 4 bajty = $2^{12}$ bajtów = 4KiB

- Proces używa 1GiB przestrzeni dyskowej
  => 1GiB / 4KiB = $2^{30} / 2^{12} = 2^{18}$ stron

A więc musimy mieć 2^18 wpisów w tablicy drugiego poziomu.
Każdy wpis zajmuje 2^2 B.
Więc minimalny rozmiar tablicy drugiego poziomu wynosi 2^18 * 2^2 B = 2^20 B

**Minimum**:
Uzyskujemy gdy strony ułożone są spójnie w przestrzeni wirtualnej, zapełniając kolejne tablice L2 po kolei. Wtedy potrzebujemy jak najmniej tablic L2. Katalog ma 1024 wpisy, każdy pokrywa 1/1024 przestrzeni adresowej = 4 MiB / 1024 = 4 MiB wirtualnej pamięci na tablicę L2. Liczba potrzebnych tablic L2:

1 GiB / (4 GiB / 1024) = 1024 / 4 = 256 tablic

Rozmiar = 4 KiB + 256/1024 × 4 MiB = 4 KiB + 1 MiB = **1 MiB + 4 KiB**

**Maksimum**: uzyskujemy gdy zaalokowanych jest jak najwięcej tablic L2. Wystarczy umieścić po jednej stronie w każdej z 1024 tablic L2 (mamy $2^{18}$ stron, więc możemy sobie na to pozwolić). Wtedy wszystkie 1024 tablice L2 są aktywne:

4 KiB + 4 MiB = **4 MiB + 4 KiB**


### Zadanie 4
![](https://hackmd.io/_uploads/rJKsCwsJGl.png)

---

TLB zawiera 64 wpisy, ma 4 wpisy na zbiór (bo jest czterodrożne), czyli ma 64 / 4 = 16 zbiorów.

**Wariant optymistyczny**:
Zakładamy, że program korzysta ze stron rozłożonych tak, że trafiają do różnych zestawów TLB — żaden zestaw nie jest przepełniony. Wtedy wszystkie 64 wpisy są użyteczne.

*64 wpisy $\times$ 4KiB = 256KiB*

**Wariant pesymistyczny**:
Wszystkie strony programu mapują się do tego samego zestawu TLB (zestaw ma tylko 4 miejsca). Wtedy TLB efektywnie zapamiętuje tylko 4 strony.

*4 wpisy $\times$ 4KiB = 16KiB*

**Z dużymi stronami (huge pages = 4MiB)**
Zamiast stron 4 KiB używamy stron 4MiB = $2^{22}$ bajtów. Liczba wpisów TLB się nie zmienia, ale każdy wpis pokrywa teraz większy obszar pamięci.

Optymistyczny: 64 $\times$ 4MiB = 256MiB
Pesymistyczny: 4 $\times$ 4MiB = 16MiB

### Zadanie 5
![](https://hackmd.io/_uploads/S16jRvs1fe.png)

### Zadanie 6
![](https://hackmd.io/_uploads/SJbh0vikfe.png)

### Zadanie 7
![](https://hackmd.io/_uploads/SkGpAwjyMl.png)

### Zadanie 8
![](https://hackmd.io/_uploads/H1thAPoJGx.png)
