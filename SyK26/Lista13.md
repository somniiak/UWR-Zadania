# Lista 13

### Zadanie 1
![](https://hackmd.io/_uploads/rk07sxrgMx.png)

**Ramka** - jeden slot w pamięci fizycznej RAM — miejsce, gdzie system może przechować jedną stronę.

**Błąd strony** - sytuacja, gdy procesor chce odczytać stronę, ale jej nie ma w żadnej ramce w RAM.

---

**a) FIFO**:
FIFO usuwa stronę, która najdłużej przebywa w pamięci (kolejka).
```
[]: 0 - miss
[0]: 1 - miss
[0, 1]: 7 - miss
[0, 1, 7]: 2 - miss
[0, 1, 7, 2]: 3 - miss
[1, 7, 2, 3]: 2 - hit
[1, 7, 2, 3]: 7 - hit
[1, 7, 2, 3]: 1 - hit
[1, 7, 2, 3]: 0 - miss
[7, 2, 3, 0]: 3 - hit
```
*miss: 6*

**b) LRU**:
LRU usuwa stronę, która była używana najdawniej (śledzi historię użyć).
```
[]: 0 - miss
[0]: 1 - miss
[0, 1]: 7 - miss
[0, 1, 7]: 2 - miss
[0, 1, 7, 2]: 3 - miss
[1, 7, 2, 3]: 2 - hit
[1, 7, 3, 2]: 7 - hit
[1, 3, 2, 7]: 1 - hit
[3, 2, 7, 1]: 0 - miss
[2, 7, 1, 0]: 3 - miss
```
*miss: 7*


### Zadanie 2
![](https://hackmd.io/_uploads/ryf4jlrxfx.png)

---

**Algorytm drugiej szansy** - Jest to modyfikacja algorytmu FIFO. W standardowym algorytmie FIFO wybierana jest pierwsza strona z kolejki, natomiast w algorytmie drugiej szansy sprawdzany jest bit odniesienia R:
- Jeżeli `R==0` (brak odniesienia) to strona jest wybierana na ofiarę.
- Jeżeli `R==1` (odniesienie) to:
  * R ustawiany jest na zero
  * Strona przesunięta jest na koniec kolejki ("otrzymała drugą szansę").
  * Przechodzimy do kolejnej strony w kolejce.

---

**Dane** *(id_ramki, czas_załadowania, bit_R)*:
`(B,3,1), (C,7,1), (D,8,0), (E,12,1), (F,14,1), (G,15,0), (H,18,1), (A,20,1)`

Ostatnie odwołanie dotyczyło ramki **A**.

`B` i `C` mają ustawiony bit R=1, co oznacza, że były niedawno używane. Podstaną jeszcze drugą szansę. G jest w kolejce za D - wskazówka idzie po kolei od najstarszej i zatrzymuje się przy pierwszym napotkanym `R=0`, czyli przy `D`. Do `G` w ogóle nie dochodzi.

**Odpowiedź**: ofiarą zostaje ramka D.


### Zadanie 3
![](https://hackmd.io/_uploads/BkvVseBgGe.png)

---

**Szamotanie** *(trashing)* - Zjawisko występujące jeśli suma zbiorów roboczych wszystkich procesów, wraz z pamięcią wykorzystywaną przez system, przekroczy choć minimalnie dostępną pamięć fizyczną komputera - następuje wtedy katastrofa. Algorytm zastępowania stron zaczyna wtedy działać na niekorzyść systemu, powodując wielką liczbę wyjątków braku strony. Drastycznie zmniejsza to wydajność pracy systemu.

**Clock** - Algorytm drugiej szansy jest rozsądny, jest on niepotrzebnie nieefektywny, ponieważ stale przesuwa strony na swojej liście. Lepszym rozwiązaniem jest przechowywanie wszystkich ramek stron na liście cyklicznej w formie zegara (jak na rysunku). Wskazówka wskazuje na najstarszą stronę. W przypadku wystąpienia błędu strony, strona wskazywana przez wskazówkę jest sprawdzana. Jeśli jej bit `R` wynosi `0`, strona jest usuwana, nowa strona jest wstawiana do zegara w jej miejsce, a wskazówka jest przesuwana o jedną pozycję. Jeśli `R` wynosi `1`, jest czyszczona, a wskazówka jest przesuwana do następnej strony. Ten proces jest powtarzany, aż zostanie znaleziona strona z `R = 0`.

![](https://hackmd.io/_uploads/BJhQvwHgzl.png)

---

**Dane**:
- Pamięć fizyczna: < 512 ramek, zakładamy - 500
- `0, 1, ..., 511, 431, 0, 1, ..., 511, 332, 0, 1, ...` (ciąg złożony z powtórzeń sekwencyjnego podciągu `0, 1, ..., 511`, pomiędzy którymi pojawiają się pojedyncze odniesienia do losowo wybranych stron, np. `431`, `332`)

**a) Dlaczego pojawia się trashing?**
`LRU`, `FIFO` i `Clock` zakładają, że to, co było niedawno używane, wkrótce znowu będzie potrzebne. Przy ciągu `0 ,1, ..., 511` ta zasada nie zachodzi: każda strona używana jest raz na 512 kroków. 500 ramek nie starcza na wszystkie 512 stron, więc przy przejściu przez strony 500–511 wyrzucane są strony 0–11, które są potrzebne jako pierwsze w następnym cyklu. Skutkuje to praktycznie 100% błędami strony - *thrashing*.

**b) Jak zapobiec trashingowi?**
Mamy 512 stron, 500 ramek. Brakuje 12. Przy każdym cyklu algorytm musi coś wyrzucić, żeby zrobić miejsce - i zawsze wybiera źle.

np. w RAM mamy strony 100–499 i 500–511 właśnie wchodzą. LRU musi zrobić miejsce, więc wyrzuca strony 100, 101, 102... bo są najstarsze. Ale w następnym cyklu sekwencja zaczyna się od 0 czyli strony 100, 101, 102 będą zaraz potrzebne. LRU wyrzucił właśnie to, co za chwilę wróci.

Zamiast wyrzucać najstarszą stronę, możemy wyrzucać najświeższą - tę, która właśnie weszła. Bo strona, która właśnie weszła (np. strona 499), będzie potrzebna dopiero za prawie cały następny cykl. Stara strona (np. 1) wróci dużo szybciej.

Przy MRU i 500 ramkach, po pierwszym załadowaniu pamięci, w każdym cyklu błędy strony wystąpią tylko dla pierwszych 12 stron (0–11), bo ramki są już zajęte przez strony z poprzedniego cyklu.

Miss rate = 12 błędów / 512 odwołań $\approx$ 2,3% (zamiast $\approx$ 100% przy LRU)

### Zadanie 4
![](https://hackmd.io/_uploads/rJhVoxrgMl.png)

---
**Anomalia Bélády'ego** - zjawisko, w którym zwiększenie liczby ramek powoduje wzrost liczby błędów strony

**Własność inkluzji** - warunek, który musi spełniać algorytm, żeby nigdy nie wykazywał anomalii Bélády'ego. Zbiór stron w pamięci dla `N` ramek musi być podzbiorem zbioru stron dla `N+1` ramek - w każdym momencie działania programu.

**Algorytmy stosowe** *(stack algorithms)* - algorytm, który spełnia własność inkluzji.

**Ciąg odwołań:** `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`

---

**a) FIFO – 3 ramki vs 4 ramki**

**FIFO, 3 ramki:**
```
1 → błąd, RAM: [1]
2 → błąd, RAM: [1,2]
3 → błąd, RAM: [1,2,3]
4 → błąd, wyrzuć 1, RAM: [2,3,4]
1 → błąd, wyrzuć 2, RAM: [3,4,1]
2 → błąd, wyrzuć 3, RAM: [4,1,2]
5 → błąd, wyrzuć 4, RAM: [1,2,5]
1 → trafienie
2 → trafienie
3 → błąd, wyrzuć 1, RAM: [2,5,3]
4 → błąd, wyrzuć 2, RAM: [5,3,4]
5 → trafienie
```
**Wynik: 9 błędów**


**FIFO, 4 ramki:**
```
1 → błąd, RAM: [1]
2 → błąd, RAM: [1,2]
3 → błąd, RAM: [1,2,3]
4 → błąd, RAM: [1,2,3,4]
1 → trafienie
2 → trafienie
5 → błąd, wyrzuć 1, RAM: [2,3,4,5]
1 → błąd, wyrzuć 2, RAM: [3,4,5,1]
2 → błąd, wyrzuć 3, RAM: [4,5,1,2]
3 → błąd, wyrzuć 4, RAM: [5,1,2,3]
4 → błąd, wyrzuć 5, RAM: [1,2,3,4]
5 → błąd, wyrzuć 1, RAM: [2,3,4,5]
```
**Wynik: 10 błędów**

Zauważamy anomalię Bélády'ego: więcej ramek (4) dało więcej błędów (10) niż mniej ramek (3) dało błędów (9).

---

**b) LRU – 3 ramki vs 4 ramki**

**LRU, 3 ramki:**
```
1 → błąd, RAM: [1]
2 → błąd, RAM: [1,2]
3 → błąd, RAM: [1,2,3]
4 → błąd, wyrzuć 1 (LRU), RAM: [2,3,4]
1 → błąd, wyrzuć 2 (LRU), RAM: [3,4,1]
2 → błąd, wyrzuć 3 (LRU), RAM: [4,1,2]
5 → błąd, wyrzuć 4 (LRU), RAM: [1,2,5]
1 → trafienie, RAM: [2,5,1]
2 → trafienie, RAM: [5,1,2]
3 → błąd, wyrzuć 5 (LRU), RAM: [1,2,3]
4 → błąd, wyrzuć 1 (LRU), RAM: [2,3,4]
5 → błąd, wyrzuć 2 (LRU), RAM: [3,4,5]
```
**Wynik: 10 błędów**

**LRU, 4 ramki:**
```
1 → błąd, RAM: [1]
2 → błąd, RAM: [1,2]
3 → błąd, RAM: [1,2,3]
4 → błąd, RAM: [1,2,3,4]
1 → trafienie, RAM: [2,3,4,1]
2 → trafienie, RAM: [3,4,1,2]
5 → błąd, wyrzuć 3 (LRU), RAM: [4,1,2,5]
1 → trafienie, RAM: [4,2,5,1]
2 → trafienie, RAM: [4,5,1,2]
3 → błąd, wyrzuć 4 (LRU), RAM: [5,1,2,3]
4 → błąd, wyrzuć 5 (LRU), RAM: [1,2,3,4]
5 → błąd, wyrzuć 1 (LRU), RAM: [2,3,4,5]
```
**Wynik: 8 błędów**

LRU nie wykazuje anomalii — więcej ramek dało mniej lub tyle samo błędów.

---

**c) Własność inkluzji**

Porównanie wyników:

| Algorytm | 3 ramki | 4 ramki | Anomalia |
|---|---|---|---|
| FIFO | 9 | 10 | TAK |
| LRU | 10 | 8 | NIE |

**Własność inkluzji** - zawartość pamięci dla N ramek musi być podzbiorem zawartości pamięci dla `N+1` ramek w każdym momencie wykonania. Formalnie:

$$
S(N, t) \subseteq S(N+1, t) \text{ dla każdego } t
$$

Jeśli ta własność zachodzi, dodanie kolejnej ramki nigdy nie może zwiększyć liczby błędów, bo wszystko co było w `N` ramkach jest też w `N+1` ramkach, a ta dodatkowa ramka może tylko pomóc.

LRU zawsze trzyma w pamięci N stron, które były używane najniedawniej. Przy `N+1` ramkach trzyma te same N stron plus jedną dodatkową (następną w kolejności "świeżości"). Zbiór dla `N` ramek jest więc zawsze podzbiorem zbioru dla `N+1` ramek.

FIFO decyduje o wyrzuceniu na podstawie czasu załadowania, nie czasu użycia. Dodanie ramki zmienia kolejność i moment wyrzucania stron - może się zdarzyć, że strona, która przy N ramkach siedziała w RAM, przy `N+1` ramkach zostaje wyrzucona wcześniej. Zbiory stron dla `N` i `N+1` ramek mogą być całkowicie różne, co łamie własność inkluzji.

### Zadanie 5
![](https://hackmd.io/_uploads/rJoUjxSxfg.png)

### Zadanie 6
![](https://hackmd.io/_uploads/ry8vslBlGg.png)

### Zadanie 7
![](https://hackmd.io/_uploads/HJYBjeHgfg.png)

---

**WSClock** łączy  strukturę zegara (okrągła lista ramek, wskazówka) z informacją o zbiorze roboczym (czas ostatniego użycia każdej strony). Każda ramka na liście przechowuje trzy rzeczy: bit R, bit M (brudna/czysta) oraz znacznik czasu ostatniego użycia.

*Algorytm drugiej szansy* (i *Clock*) patrzy tylko na bit R — strona jest kandydatką gdy R=0, niezależnie od tego kiedy była ostatnio używana. WSClock dodaje do tego czas - sama wartość R=0 nie wystarczy, strona musi być też wystarczająco "stara" (wiek > τ), żeby ją wyrzucić. Dzięki temu WSClock ma pojęcie o tym, które strony są aktywnie potrzebne, a nie tylko czy były tknięte w ostatnim obrocie zegara.

Działanie:
- `R=1` -> strona była niedawno używana, należy do zbioru roboczego. Wyzeruj R, przesuń wskazówkę dalej.
- `R=0`, `wiek > τ`, strona czysta -> strona poza zbiorem roboczym i kopia jest na dysku. Zastępujemy nową stroną.
- `R=0`, `wiek > τ`, strona brudna -> ...
- `R=0`, `wiek <= τ` -> strona wciąż w zbiorze roboczym, oszczędzamy ją. Zapamiętaj ją jako kandydatkę z najstarszym znacznikiem czasu i idź dalej.
