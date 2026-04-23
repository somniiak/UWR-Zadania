# Lista 8

### Zadanie 1
![](https://hackmd.io/_uploads/Hy5FQo8TZl.png)

---

**Hazard sterowania**
Pojawia się przy instrukcjach skoku kiedy przy złej predykcji wykonają się kolejne niepotrzebne instrukcje, które trzeba będzie potem sflushować.

**Hazard strukturalny**
Pojawia się, gdy dwa lub więcej etapów potoku chce jednocześnie użyć tego samego zasobu sprzętowego (np. jednego ALU).

**RAW** *(read after write)*
Instrukcja próbuje odczytać rejestr, który poprzednia instrukcja jeszcze nie zdążyła zapisać (zaktualizować jego wartość).

**WAR** *(write after read)*
Druga instrukcja w kolejce instrukcji do wykonania będzie chciała zapisać do tego samego rejestru, z którego pierwsza instrukcja nie zdążyła jeszcze odczytać starej wartości.

**WAW** *(write after write)*
Druga instrukcja zapisuje do tego samego rejestru, do którego zapisuje pierwsza. Późniejsza instrukcja może zapisać wynik wcześniej niż poprzednia co powoduje zły końcowy stan rejestru.

---

**a) Procesor jednocyklowy**

Brak hazardów. Każda instrukcja wykonuje się w jednym, niepodzielnym cyklu. Kolejna instrukcja startuje dopiero gdy poprzednia jest w pełni zakończona (zapis do rejestrów następuje przed pobraniem kolejnej instrukcji).

**b) Procesor potokowy (z pojedynczym ALU)**

- Hazard sterowania $\small(+\small)$

  Nie wiemy czy wykonać kolejne instrukcje po skoku dopóki nie uzyskamy wyniku operacji warunkowej.

  ```.
  beq s0, s1, LABEL   # adres skoku znany po fazie EX
  add t1, s2, s3      # instrukcja już pobrana, może być błędna
  ```

- Hazard strukturalny $\small(-\small)$:

  Zakładając, że nie mamy współdzielonej pamięci instrukcji i danych, fazy `Fetch` i `Execute` nigdy nie konkurują o ten sam zasób. Jedyne ALU jest używane tylko w fazie EX, przez jedną instrukcję naraz.

- RAW $\small(+\small)$:

  ```.
  add  s0, s2, s3   # add: 5 cykli
  add  t0, s0, s1   # potrzebuje s0, które nie jest gotowe
  ```

- WAR/WAW $\small(-\small)$:

  Instrukcje kończą się w tej samej kolejności, w jakiej zostały wydane. Nie ma mechanizmu, który pozwoliłby późniejszej instrukcji zapisać rejestr przed wcześniejszą.

**c) Procesor potokowy (z wieloma jednostkami wykonawczymi)**

- Hazard sterowania $\small(+\small)$:

  Analigocznie do punktu **(b)**.

- Hazard strukturalny $\small(+\small)$:

  ```.
  mul t1, s0, s1    # zakładamy, że jest tylko jedna jednostka mnożenia
  mul t2, s2, s3    # dwie instrukcje próbują z niej skorzystać
  ```

- RAW $\small(+\small)$:

  Analigocznie do punktu **(b)**.

- WAR $\small(+\small)$:

  ```.
  add  t1, s0, s1   # instrukcja 1: odczytuje s1 w późnej fazie
  mul  s1, s2, s3   # instrukcja 2: szybka jednostka zapisuje s1 wcześniej niż
                    # instrukcja 1 je odczyta
  ```

- WAW $\small(+\small)$:

  ```.
  add  t1, s0, s1   # instrukcja 1: zapisuje t1 po 4 cyklach
  mul  t1, s2, s3   # instrukcja 2: zapisuje t1 po 1 cyklu (szybsza jednostka)
                    # instrukcja 2 zapisuje t1 przed instrukcją 1
  ```

### Zadanie 2
![](https://hackmd.io/_uploads/H1rTroUa-e.png)

```.=
t1 = *s0          # lw
t2 = t1 + s1      # add
t1 = s2 - s3      # sub
t3 = t1 & s4      # and
t4 = *(s0 + 4)    # lw
t5 = t2 | t4      # or
```

---

**1. Identyfikacja zależności danych**

- **RAW:**
    - `t1` (Instrukcja 1->2): `t2` potrzebuje wyniku `lw` z instrukcji 1.
    - `t1` (Instrukcja 3->4): `t3` potrzebuje wyniku `sub` z instrukcji 3.
    - `t2` (Instrukcja 2->6): `t5` potrzebuje wyniku z instrukcji 2.
    - `t4` (Instrukcja 5->6): `t5` potrzebuje wyniku `lw` z instrukcji 5.
- **WAW:**
    - `t1` (Instrukcja 1->3): Obie instrukcje zapisują do tego samego rejestru.
- **WAR:**
    - `t1` (Instrukcja 2->3): Instrukcja 3 nadpisuje `t1`, zanim instrukcja 2 go odczyta (w potoku).

---

**2. Rearanżacja bez przemianowywania rejestrów**

Musimy zachować kolejność zapisu do `t1` oraz zapewnić, że instrukcja 2 odczyta poprawną wartość przed jej nadpisaniem przez instrukcję 3. Uwzględniamy opóźnienie `lw` ($n \to n+2$) oraz zwykły forwarding ($n \to n+1$).

| Cykl | Instrukcja 1 | Instrukcja 2 | Uwagi |
| :--- | :--- | :--- | :--- |
| **1** | `t1 = *s0` (1) | `t4 = *(s0+4)` (5) | Dwa odczyty z pamięci naraz. |
| **2** | `nop` | `nop` | Oczekiwanie na dane z `lw` (cykl $n+2$). |
| **3** | `t2 = t1 + s1` (2) | `nop` | RAW (1->2) gotowe. Instrukcja 3 nie może być tu (WAR z 2). |
| **4** | `t1 = s2 - s3` (3) | `t5 = t2 \| t4` (6) | RAW (2->6) i (5->6) gotowe. |
| **5** | `t3 = t1 * s4` (4) | `nop` | RAW (3->4) gotowe. |

**Miara IPC (Instructions Per Cycle):**
Program składa się z 6 instrukcji wykonanych w 5 cyklach.
$IPC = \frac{6}{5} = 1,2$.

---

**3. Rearanżacja z przemianowywaniem rejestrów**

Używamy rejestru pomocniczego (np. `r1`), aby wyeliminować zależności WAW i WAR na rejestrze `t1`.

Zmieniony kod:
3. `r1 = s2 - s3`
4. `t3 = r1 * s4`

| Cykl | Instrukcja 1 | Instrukcja 2 | Uwagi |
| :--- | :--- | :--- | :--- |
| **1** | `t1 = *s0` (1) | `t4 = *(s0+4)` (5) | |
| **2** | `r1 = s2 - s3` (3) | `nop` | Instrukcja 3 może być wcześniej dzięki renamingowi. |
| **3** | `t2 = t1 + s1` (2) | `t3 = r1 * s4` (4) | RAW (1->2) i (3->4) gotowe. |
| **4** | `t5 = t2 \| t4` (6) | `nop` | RAW (2->6) i (5->6) gotowe. |

**Nowe IPC:**
6 instrukcji w 4 cyklach.
$IPC = \frac{6}{4} = 1,5$.

**Przyspieszenie:**
$\frac{1,5}{1,2} = 1,25$
Program z przemianowywaniem rejestrów jest o **25% szybszy**.

### Zadanie 3
![](https://hackmd.io/_uploads/B1K9ms86bx.png)

---

**1. Identyfikacja zależności danych**

- **RAW:**
    - `t1`: (1 $\to$ 2) – instrukcja 2 potrzebuje wyniku ładowania.
    - `t2`: (2 $\to$ 3) – instrukcja 3 potrzebuje wyniku dodawania.
    - `t1`: (3 $\to$ 4) – instrukcja 4 potrzebuje wyniku dodawania.
    - `t2`: (5 $\to$ 6) – instrukcja 6 potrzebuje wyniku ładowania.
- **WAW:**
    - `t1`: instrukcje 1 i 3.
    - `t2`: instrukcje 2 i 5.
- **WAR:**
    - `t1`: instrukcja 2 czyta `t1`, zanim instrukcja 3 go nadpisze.
    - `t2`: instrukcja 3 czyta `t2`, zanim instrukcja 5 go nadpisze.

---

**2. Rearanżacja bez przemianowywania rejestrów**

| Cykl | Instrukcja 1 | Instrukcja 2 | Uwagi |
| :--- | :--- | :--- | :--- |
| **1** | `t1 = *s0` (1) | `nop` | Start ładowania `t1`. |
| **2** | `nop` | `nop` | Oczekiwanie na `t1` (opóźnienie `lw`). |
| **3** | `t2 = t1 + s1` (2) | `nop` | RAW (1->2) gotowe. |
| **4** | `t1 = t2 + s2` (3) | `nop` | RAW (2->3) gotowe. |
| **5** | `*(s0+4) = t1` (4) | `t2 = *(s0+8)` (5) | RAW (3->4) gotowe. Start ładowania (5). |
| **6** | `nop` | `nop` | Oczekiwanie na `t2` (opóźnienie `lw`). |
| **7** | `t3 = t2 - s3` (6) | `nop` | RAW (5->6) gotowe. |

**Wynik:**
* **Czas wykonania:** 7 cykli.
* **IPC:** $\frac{6}{7} \approx 0,86$.

---

**3. Rearanżacja z przemianowywaniem rejestrów**

Używamy rejestrów pomocniczych `r1` i `r2`.
* Instrukcja 3 zapisuje do `r1` zamiast `t1`.
* Instrukcja 5 zapisuje do `r2` zamiast `t2`.

Zmieniony kod:
1. `t1 = *s0`
2. `t2 = t1 + s1`
3. `r1 = t2 + s2`
4. `*(s0+4) = r1`
5. `r2 = *(s0+8)`
6. `t3 = r2 - s3`

Dzięki temu instrukcje (5) i (6) stają się niezależne od głównego ciągu (1-4) i mogą zostać wykonane wcześniej.

| Cykl | Instrukcja 1 | Instrukcja 2 | Uwagi |
| :--- | :--- | :--- | :--- |
| **1** | `t1 = *s0` (1) | `r2 = *(s0+8)` (5) | Dwa ładowania równolegle. |
| **2** | `nop` | `nop` | Czekamy na oba wyniki `lw`. |
| **3** | `t2 = t1 + s1` (2) | `t3 = r2 - s3` (6) | Dane z (1) i (5) są gotowe. |
| **4** | `r1 = t2 + s2` (3) | `nop` | RAW (2->3) przez forwarding. |
| **5** | `*(s0+4) = r1` (4) | `nop` | RAW (3->4) przez forwarding. |

**Wynik:**
* **Nowe IPC:** $\frac{6}{5} = 1,2$.
* **Przyspieszenie:** $\frac{1,2}{0,86} \approx 1,4$ (czyli o **40%** szybciej).

Przemianowywanie rejestrów pozwoliło na równoległe potraktowanie dwóch niezależnych ciągów obliczeń, które wcześniej blokowały się nawzajem przez użycie tych samych nazw rejestrów (`t1`, `t2`).


### Zadanie 4
![](https://hackmd.io/_uploads/ByriXjUabl.png)

---

**Scoreboard** to układ, który patrzy się na pewną grupę instrukcji (fragment programu) i decycuje, które instrukcje są od siebie zależne i wykonuje instrukcje w taki sposób (out-of-order), aby zminimalizować opóźnienia i zapobiegać powstawaniu hazardów.

Instrukcja przechodzi przez 4 fazy:
1. **Issue** - instrukcja jest przekazywana do wykonania, jeśli: jednostka jest wolna (brak hazardu strukturalnego) i brak hazardu WAW (żadna inna aktywna instrukcja nie pisze do tego samego rejestru).
2. **Read Operands** – instrukcja czeka aż wszystkie jej operandy źródłowe są gotowe (brak hazardu RAW), potem je odczytuje.
3. **Execute** - wykonywanie właściwych obliczeń.
4. **Write Result** – wynik jest zapisywany, ale tylko jeśli brak hazardu WAR (żaden inny aktywny odczyt nie czeka na ten rejestr).

---

**RAW**
Wykrywany w fazie *Read Operands*. Scoreboard śledzi które rejestry są aktualnie zapisywane przez aktywne instrukcje. Jeśli operand źródłowy instrukcji jest zajęty (produkowany przez wcześniejszą instrukcję), instrukcja czeka w fazie Read Operands aż wynik zostanie zapisany.

```.
mul  t1, s0, s1   # pisze t1, długo trwa
add  t2, t1, s2   # czeka w Read Operands dopóki t1 nie gotowe
```

**WAW**
Wykrywany w fazie *Issue*. Jeśli jakaś aktywna instrukcja już pisze do tego samego rejestru docelowego, nowa instrukcja nie może być wydana (stall w Issue) dopóki poprzednia nie ukończy zapisu.

```.
add  t1, s0, s1   # aktywna, jeszcze nie zapisała t1
mul  t1, s2, s3   # Issue zablokowane – WAW na t1
```

**WAR**
Wykrywany w fazie *Write Result*. Instrukcja gotowa do zapisu sprawdza czy żadna wcześniejsza instrukcja (która jeszcze nie odczytała operandów) nie czeka na odczyt tego rejestru. Jeśli tak, to czeka z zapisem.

```.
add  t1, s0, s1   # odczytuje s1 (jeszcze w Read Operands)
mul  s1, s2, s3   # gotowa do zapisu s1, ale czeka – WAR
```

### Zadanie 5
![](https://hackmd.io/_uploads/BkijQo86bx.png)

---

![](https://hackmd.io/_uploads/BknbAMwpWx.png)

**Reorder Buffer**: Instrukcje wykonywane są poza kolejnością (out-of-order), ale przed udostępnieniem wyników są uporządkowywane w kolejności oryginalnego programu.

Algorytm:
- Pobranie instrukcji i dodanie jej do kolejki.
- Równoległe obliczanie instrukcji, jeśli jej zasoby są dostępne, ale bez zapisywania wyników w rejestrach docelowych.
- Gdy instrukcja z góry kolejki jest gotowa, zapisujemy jej wynik do docelowego rejestru i usuwamy z kolejki.

Rozwiązywanie hazardów:
- **RAW**: Instrukcja, która potrzebuje wyniku jeszcze niewykonanej operacji, czeka w stacji rezerwowej.
- **WAR**: Każda instrukcja operuje na swoim slocie w ROB, a zapis do rejestru architektonicznego następuje dopiero przy Commit, w kolejności programowej. Nie ma sytuacji gdzie późniejsza instrukcja nadpisałaby rejestr przed odczytem przez wcześniejszą.
- **WAW**: Commit następuje zawsze w kolejności programowej (FIFO), więc ostatni zapis do rejestru zawsze będzie wynikiem instrukcji najpóźniejszej w kolejności programu

![](https://hackmd.io/_uploads/BJzE8Hvpbg.png)

| Cecha | Scoreboard | Reorder Buffer (ROB) |
| :--- | :--- | :--- |
| **Zależności RAW** | Powodują wstrzymanie (stalli) w fazie odczytu operandów. | Obsługiwane przez forwarding; instrukcje czekają tylko na dane, nie na fazy. |
| **Zależności WAR** | Wstrzymują zapis wyniku (Write Back), dopóki poprzednie instrukcje nie odczytają danych. | Eliminowane przez renaming. Wynik trafia do ROB, nie blokując potoku. |
| **Zależności WAW** | Wstrzymują zlecenie instrukcji (Issue), jeśli rejestr docelowy jest zajęty. | Każda instrukcja dostaje własny wpis w ROB, nadpisywanie nie koliduje. |
| **Kolejność zatwierdzania** | Wyniki są wpisywane do rejestrów zaraz po zakończeniu wykonania (może być poza kolejnością). | Wyniki są zatwierdzane zawsze w kolejności programowej. |

ROB jest wydajniejszy, ponieważ usuwa sztuczne przestoje (stalls) wywołane hazardami WAR i WAW, na które Scoreboard jest podatny.

### Zadanie 6
![](https://hackmd.io/_uploads/H14ABsUaWx.png)

### Zadanie 7
![](https://hackmd.io/_uploads/S1RiXsIpWl.png)
