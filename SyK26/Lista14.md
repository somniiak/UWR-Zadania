# Lista 14

## Zadanie 1
![](https://hackmd.io/_uploads/HyGs1kZWGg.png)

---

### Pojęcia

**Zmiana kontektsu** (*context switch*) -- operacja polegająca na zapisaniu stanu bieżącego procesu (zawartości rejestrów, licznika rozkazów, wskaźnika stosu) do jego PCB (*Process Control Block*) i wczytaniu stanu innego procesu. Jest to czas stracony - w trakcie zmiany kontekstu procesor nie wykonuje żadnej użytecznej pracy.

**Proces ograniczony przez dostęp do procesora** (*CPU-bound process*) -- proces, który większość czasu spędza na obliczeniach, rzadko wykonuje I/O.

**Proces ograniczony przez wejście-wyjście** (*Input-Output bound process*) -- proces, króry większość czasu spędza na oczekiwaniu na zakończenie operacji wejścia-wyjścia.

**Proces interaktywny** -- komunikuje się z użytkownikiem w czasie rzeczywistym, musi reagować szybko, wymaga niskich opóźnień.

**Proces wsadowy** (*batch process*) -- nie wymaga interakcji z użytkownikiem, może czekać. Liczy się całkowity czas wykonania, nie responsywność.

---

### Planowanie wywłaszczające a niewywłaszczające

![](https://hackmd.io/_uploads/rkeqJSwZze.jpg)

**Planowanie wywłaszczające** (*preemptive scheduling*) -- system operacyjny może przerwać proces w dowolnym momencie i przenieść go z powrotem do kolejki gotowych (wszystkie powyższe punkty).

**Planowanie niewywłaszczające** (*non-preemptive scheduling*) -- proces, który dostał procesor, trzyma go aż do momentu, gdy sam go zwolni — przez zakończenie lub przejście do stanu czekającego (dobrowolnie oddaje sterowanie) (punkty 1 i 4).

**Diagram stanów procesów** - pokazuje w jaki sposób może nastąpić przejście pomiędzy stanami. Ze stanu `new` po utworzeniu procesu możemy przejśc wyłącznie do stanu `ready`, żeby znaleźć się w stanie `terminated` musimy być wczenśniej w stanie `running` - proces wykonywał się na procesorze i nagle (dzieje się coś co sprawia, że) proces kończy pracę. Ze stanu `running` można jescze przejść do dwóch innych stanów: `ready` - zachodzi tzw. "*przerwanie*", `waiting` - operacja I/O.

![](https://hackmd.io/_uploads/ryy8i4PbGx.png)

---

### Dlaczego planowanie wywłaszczające jest popularniejsze?

Mimo wyższej złożoności implementacji planowanie wywłaszczające dominuje z kilku powodów:
- Umożliwia responsywność systemu — jeden proces obciążający CPU nie zablokuje całego systemu na czas swojego wykonania. W planowaniu niewywłaszczającym jeden błędny/długotrwały lub złośliwy proces zajmować procesor przez długi czas.
- Pozwala na obsługę priorytetów — gdy pojawia się zadanie o wysokim priorytecie (np. obsługa przerwania), system może natychmiast przekazać mu procesor.
- Na wielordzeniowych systemach z wieloma procesami interaktywnymi brak wywłaszczania oznaczałby niedopuszczalnie długie czasy odpowiedzi dla użytkownika

![](https://hackmd.io/_uploads/ryXTJdDWfl.png)


## Zadanie 2
![](https://hackmd.io/_uploads/HJPiykbWfl.png)

---

<center>
<table>
  <thead>
    <tr>
      <th>Algorytmy planowania niewywłaszczającego</th>
      <th>Algorytmy planowania wywłaszczającego</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>FCFS</b> (<i>First Come First Served</i>) - pierwszy zgłoszony, pierwszy obsłużony.</td>
      <td><b>Planowanie rotacyjne</b> (<i>Round Robin, RR</i>) - po ustalonym kwancie czasu proces wykonywany jest przerywany i trafia do kolejki procesów gotowych.</td>
    </tr>
    <tr>
      <td><b>LCFS</b> (<i>Last Come First Served</i>) - ostatni zgłoszony, pierwszy obsłużony.</td>
      <td><b>SRTF</b> (<i>Shortest Remaining Time First</i>) - najpierw zadanie, które ma najkrótszy czas do zakończenia.</td>
    </tr>
    <tr>
      <td><b>SJF</b> (<i>Shortest Job First</i>) - najpierw najkrótsze zadanie.</td>
      <td></td>
    </tr>
  </tbody>
</table>
</center>

---

**Wykorzystanie procesora** (*CPU utilization*) -- procent czasu, w którym procesor wykonuje użyteczną pracę (nie jest bezczynny).

-  Maksymalne wykorzystanie CPU może osiągnąć np. przez bardzo duże kwanty czasu w RR, co pogarsza czas odpowiedzi procesów interaktywnych.

**Przepustowość** (*Throughput*) -- liczba procesów kończonych w jednostce czasu.

- Algorytm SJF maksymalizuje `throughput`, preferując krótkie procesy, ale może głodzić długie procesy - ich czas oczekiwania rośnie w nieskończoność

**Czas cyklu przetwarzania** (*Turnaround time*) -- czas od momentu wprowadzenia procesu do systemu do chwili jego zakończenia. Obejmuje czas oczekiwania w kolejce, czas wykonania CPU oraz czas ewentualnych operacji I/O.

- Minimalizacja średniego `turnaround` przy użyciu SJF faworyzuje krótkie procesy kosztem długich.

**Czas oczekiwania** (*Waiting time*) -- czas spędzony przez proces w kolejce gotowości.

- Algorytm FCFS daje małe `waiting time` przy jednym długim procesie, ale duże dla wszystkich pozostałych.

**Czas odpowiedzi** (*Response time*) -- czas pomiędzy przedłożeniem
żądania, a rozpoczęciem przekazywania odpowiedzi.

- Round Robin minimalizuje response time (każdy proces dostaje CPU szybko), ale zwiększa turnaround przez narzut zmian kontekstu.


## Zadanie 3
![](https://hackmd.io/_uploads/BkTGZkbWfx.png)

---

Wszystkie procesy przybyły w chwili 0, w kolejności $P1$, $P2$, $P3$, $P4$, $P5$.

<center>

| Proces | Burst Time | Priority |
|--------|-----------|----------|
| $P1$ | 2 | 2 |
| $P2$ | 1 | 1 |
| $P3$ | 8 | 4 |
| $P4$ | 4 | 2 |
| $P5$ | 5 | 3 |

</center>

**FCFS** (po kolejności przybycia): `P1: 0-2`, `P2: 2-3`, `P3: 3-11`, `P4: 11-15`, `P5: 15-20`

```
┌────┬──┬────────────────┬────────┬──────────┐
│ P1 │P2│       P3       │   P4   │    P5    │
└────┴──┴────────────────┴────────┴──────────┘
0    2  3                11       15         20
```

**SJF** (sortowanie po burst time): `P2: 0-1`, `P1: 1-3`, `P4: 3-7`, `P5: 7-12`, `P3: 12-20`

```
┌──┬────┬────────┬──────────┬────────────────┐
│P2│ P1 │   P4   │    P5    │       P3       │
└──┴────┴────────┴──────────┴────────────────┘
0  1    3        7          12               20
```

**Priorytetowy bez wywłaszczeń** (po priorytecie, przy równym - kolejność przybycie): `P3: 0-8`, `P5: 8-13`, `P1: 13-15`, `P4: 15-19`, `P2: 19-20`

```
┌────────────────┬──────────┬────┬────────┬──┐
│       P3       │    P5    │ P1 │   P4   │P2│
└────────────────┴──────────┴────┴────────┴──┘
0                8          13   15       19  20
```

**Round Robin (Q=2)** (kolejka: P1, P2, P3, P4, P5):
```
t=0: P1 (burst=2) -> kończy się w t=2
t=2: P2 (burst=1) -> kończy się w t=3
t=3: P3 (burst=8, daje 2) → t=3–5
t=5: P4 (burst=4, daje 2) → t=5–7
t=7: P5 (burst=5, daje 2) → t=7–9
t=9: P3 (burst=6, daje 2) → t=9–11
t=11: P4 (burst=2, daje 2) → kończy się t=13
t=13: P5 (burst=3, daje 2) → t=13–15
t=15: P3 (burst=4, daje 2) → t=15–17
t=17: P5 (burst=1, daje 1) → kończy się t=18
t=18: P3 (burst=2, daje 2) → kończy się t=20
```

```
┌────┬──┬────┬────┬────┬────┬────┬────┬────┬──┬────┐
│ P1 │P2│ P3 │ P4 │ P5 │ P3 │ P4 │ P5 │ P3 │P5│ P3 │
└────┴──┴────┴────┴────┴────┴────┴────┴────┴──┴────┘
0    2  3    5    7    9   11   13   15   17 18   20
```

---

**Turnaround time** -- czas od momentu wprowadzenia procesu do systemu do chwili jego zakończenia. (Tutaj: wszystkie procesy przybyły w t=0 więc turnaround to czas zakończenia.)

<center>

| FCFS | SJF | Prior. bez wywł. | RR   |
|------|-----|------------------|------|
| 10.2 | 8.6 | 15               | 11.2 |

</center>

---

**Czas oczekiwania** = turnaround − burst

<center>

| Proces | burst | FCFS | SJF | Prior. | RR Q=2 |
|--------|-------|------|-----|--------|--------|
| P1 | 2 | 0 | 1 | 13 | 0 |
| P2 | 1 | 2 | 0 | 19 | 2 |
| P3 | 8 | 3 | 12 | 0 | 12 |
| P4 | 4 | 11 | 3 | 15 | 9 |
| P5 | 5 | 15 | 7 | 8 | 13 |
| **Avg** | - | **6.2** | **4.6** | **11.0** | **7.2** |

</center>


## Zadanie 4
![](https://hackmd.io/_uploads/HknoyJb-zl.png)

## Zadanie 5
![](https://hackmd.io/_uploads/B1bh1y-WGe.png)

## Zadanie 6
![](https://hackmd.io/_uploads/BJ9n1JWZGe.png)

## Zadanie 7
![](https://hackmd.io/_uploads/Byp2Jy-ZGx.png)

## Zadanie 8
![](https://hackmd.io/_uploads/B1JT1yWWzg.png)

## Zadanie 9
![](https://hackmd.io/_uploads/rkf61k--Gl.png)
