# Lista 3

### Zadanie 1
![](https://hackmd.io/_uploads/rknk-pNc-g.png)

```=
JEŚLI P JEST UJEMNE:
  PRZESUŃ REJESTR (P, A) 1 BIT W LEWO
  DODAJ B DO P

W PRZECIWNYM PRZYPADKU:
  PRZESUŃ REJESTR (P, A) 1 BIT W LEWO
  ODEJMIJ B OD P

JEŚLI P JEST UJEMNE:
  USTAW NAJMNIEJ ZNACZĄCY BIT A NA 0

W PRZECIWNYM PRZYPADKU:
  USTAW NAJMNIEJ ZNACZĄCY BIT A NA 1
```

Powtarzając algorytm $n$ razy wynik dzielenia będzie znajdować się w A. Jeśli P jest nieujemne, będzie to reszta z dzielenia, w.p.p. należy dodać B do P, żeby otrzymać resztę.

(Kroki w linijkach 2 i 6 są takie same - kusi, żeby wyciągnać je przed instrukcje warunkowe, a dopiero potem sprawdzić znak P. To nie zadziała, bo bit znaku może być utracony przy przesuwaniu rejestrów.)

W algorytmie w wersji `restoring`, jeśli wynik odejmowania B jest liczbą ujemną - do rejestru P dodajemy z powrotem B. Wersja `non-restoring` działa z liczbami ujemnymi.

**Dowód poprawności**
![](https://hackmd.io/_uploads/rJmidF_5Wg.png)

![](https://hackmd.io/_uploads/H13ckHFqZl.png)



### Zadanie 2
![](https://hackmd.io/_uploads/SJkeWaE9-l.png)

W mnożeniu przesuwanie po zerach polega na dodatkowym sprawdzeniu czy najmniej znaczący bit rejestru A wynosi 0 i jeśli tak jest, pominięciu kroku z dodawaniem i przejściu bezpośrednio do przesuwania - stąd nazwa _przesuwanie po zerach_.

### Zadanie 3
![](https://hackmd.io/_uploads/ByXlW645bl.png)

### Zadanie 4
![](https://hackmd.io/_uploads/ByFgbTEqZx.png)

### Zadanie 5
![](https://hackmd.io/_uploads/SkfgisOc-x.png)

![](https://hackmd.io/_uploads/HyDNt3dc-e.png)

| l | $RD_∘(l)$                                                                          | $RD_•(l)$                                                                          |
|---|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 1 | {(x,?), (y,?), (i,?), (t,?), (z,?)}                                            | {(x,1), (y,?), (i,?), (t,?), (z,?)}                                            |
| 2 | {(x,1), (y,?), (i,?), (t,?), (z,?)}                                            | {(x,1), (y,2), (i,?), (t,?), (z,?)}                                            |
| 3 | {(x,1), (y,2), (i,?), (t,?), (z,?)}                                            | {(x,1), (y,2), (i,3), (t,?), (z,?)}                                            |
| 4 | {(x,1),(x,6), (y,2),(y,7), (i,3),(i,8), (t,?),(t,5), (z,?)}                   | {(x,1),(x,6), (y,2),(y,7), (i,3),(i,8), (t,?),(t,5), (z,?)}                   |
| 5 | {(x,1),(x,6), (y,2),(y,7), (i,3),(i,8), (t,?),(t,5), (z,?)}                   | {(x,1),(x,6), (y,2),(y,7), (i,3),(i,8), (t,5), (z,?)}                         |
| 6 | {(x,1),(x,6), (y,2),(y,7), (i,3),(i,8), (t,5), (z,?)}                         | {(x,6), (y,2),(y,7), (i,3),(i,8), (t,5), (z,?)}                               |
| 7 | {(x,6), (y,2),(y,7), (i,3),(i,8), (t,5), (z,?)}                               | {(x,6), (y,7), (i,3),(i,8), (t,5), (z,?)}                                      |
| 8 | {(x,6), (y,7), (i,3),(i,8), (t,5), (z,?)}                                     | {(x,6), (y,7), (i,8), (t,5), (z,?)}                                            |
| 9 | {(x,1),(x,6), (y,2),(y,7), (i,3),(i,8), (t,?),(t,5), (z,?)}                   | {(x,1),(x,6), (y,9), (i,3),(i,8), (t,?),(t,5), (z,?)}                         |

### Zadanie 6
![](https://hackmd.io/_uploads/H1sQW6N9bx.png)

**Równania dla $RD_∘(l)$**
* $RD_∘(1) = \{(z, ?), (x, ?), (y, ?), (i, ?), (t, ?)\}$
* $RD_∘(2) = RD_•(1)$
* $RD_∘(3) = RD_•(2)$
* $RD_∘(4) = RD_•(3) \cup RD_•(8)$
* $RD_∘(5) = RD_•(4)$
* $RD_∘(6) = RD_•(5)$
* $RD_∘(7) = RD_•(6)$
* $RD_∘(8) = RD_•(7)$
* $RD_∘(9) = RD_•(4)$

**Równania dla $RD_•(l)$**
* $RD_•(1) = (RD_∘(1) \setminus \{(x,\ell) \mid \ell \in \text{Lab}\}) \cup \{(x,1)\}$
* $RD_•(2) = (RD_∘(2) \setminus \{(y,\ell) \mid \ell \in \text{Lab}\}) \cup \{(y,2)\}$
* $RD_•(3) = (RD_∘(3) \setminus \{(i,\ell) \mid \ell \in \text{Lab}\}) \cup \{(i,3)\}$
* $RD_•(4) = RD_∘(4) \quad (\text{test nie modyfikuje żadnej zmiennej})$
* $RD_•(5) = (RD_∘(5) \setminus \{(t,\ell) \mid \ell \in \text{Lab}\}) \cup \{(t,5)\}$
* $RD_•(6) = (RD_∘(6) \setminus \{(x,\ell) \mid \ell \in \text{Lab}\}) \cup \{(x,6)\}$
* $RD_•(7) = (RD_∘(7) \setminus \{(y,\ell) \mid \ell \in \text{Lab}\}) \cup \{(y,7)\}$
* $RD_•(8) = (RD_∘(8) \setminus \{(i,\ell) \mid \ell \in \text{Lab}\}) \cup \{(i,8)\}$
* $RD_•(9) = (RD_∘(9) \setminus \{(y,\ell) \mid \ell \in \text{Lab}\}) \cup \{(y,9)\}$

**Sprawdzenie równań**
* Węzeł 1:
$RD_∘(1) = \{(z, ?), (x, ?), (y, ?), (i, ?), (t, ?)\}$
Przepływ przez instrukcję $[x := 0]^1$.
$RD_•(1) = (RD_∘(1) \setminus \{(x,\ell) \mid \ell \in \text{Lab}\}) \cup \{(x,1)\}$
Odejmowanie usuwa $(x,?)$ - jedyną parę dla $x$ obecną w zbiorze.
$\{(y,?),(i,?),(t,?),(z,?)\} \cup \{(x,1)\} = \{(x,1),(y,?),(i,?),(t,?),(z,?)\}$

* Węzeł 2:
$RD_∘(2) = RD_•(1) = \{(x,1),(y,?),(i,?),(t,?),(z,?)\}$
Przepływ przez instrukcję $[y := 1]^2$.
$RD_•(2) = (RD_∘(2) \setminus \{(y,\ell) \mid \ell \in \text{Lab}\}) \cup \{(y,2)\}$
Odejmowanie usuwa $(y,?)$:
$\{(x,1),(i,?),(t,?),(z,?)\} \cup \{(y,2)\} = \{(x,1),(y,2),(i,?),(t,?),(z,?)\}$

* Węzeł 3:
$RD_∘(3) = RD_•(2) = \{(x,1),(y,2),(i,?),(t,?),(z,?)\}$
Przepływ przez instrukcję $[i := 1]^3$:
$RD_•(3) = (RD_∘(3) \setminus \{(i,\ell) \mid \ell \in \text{Lab}\}) \cup \{(i,3)\}$
Odejmowanie usuwa $(i,?)$:
$\{(x,1),(y,2),(t,?),(z,?)\} \cup \{(i,3)\} = \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$

* Węzeł 4:
Dwa poprzedniki: węzeł 3 i węzeł 8.
$RD_∘(4) = RD_•(3) \cup RD_•(8)$
$\qquad \quad = \{(x,1),(y,2),(i,3),(t,?),(z,?)\} \cup \{(x,6),(y,7),(i,8),(t,5),(z,?)\}$
$\quad \quad \quad = \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$
Przepływ przez test $[i < z]^4$ - nie modyfikuje żadnej zmiennej:
$RD_•(4) = RD_∘(4) = \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$

* Węzeł 5:
$RD_∘(5) = RD_•(4) = \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$
Przepływ przez instrukcję $[t := x+y]^5$:
$RD_•(5) = (RD_∘(5) \setminus \{(t,\ell) \mid \ell \in \text{Lab}\}) \cup \{(t,5)\}$
Odejmowanie usuwa $(t,?)$ oraz $(t,5)$:
$\{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(z,?)\} \cup \{(t,5)\} =$
$\{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$

* Węzeł 6:
$RD_∘(6) = RD_•(5) = \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$
Przepływ przez instrukcję $[x := y]^6$:
$RD_•(6) = (RD_∘(6) \setminus \{(x,\ell) \mid \ell \in \text{Lab}\}) \cup \{(x,6)\}$
Odejmowanie usuwa $(x,1)$ oraz $(x,6)$:
$\{(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\} \cup \{(x,6)\} =$
$\{(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$


* Węzeł 7:
$RD_∘(7) = RD_•(6) = \{(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$
Przepływ przez instrukcję $[y := t]^7$:
$RD_•(7) = (RD_∘(7) \setminus \{(y,\ell) \mid \ell \in \text{Lab}\}) \cup \{(y,7)\}$
Odejmowanie usuwa $(y,2)$ oraz $(y,7)$:
$\{(x,6),(i,3),(i,8),(t,5),(z,?)\} \cup \{(y,7)\} =$
$\{(x,6),(y,7),(i,3),(i,8),(t,5),(z,?)\}$

* Węzeł 8:
$RD_∘(8) = RD_•(7) = \{(x,6),(y,7),(i,3),(i,8),(t,5),(z,?)\}$
Przepływ przez instrukcję $[i := i+1]^8$:
$RD_•(8) = (RD_∘(8) \setminus \{(i,\ell) \mid \ell \in \text{Lab}\}) \cup \{(i,8)\}$
Odejmowanie usuwa $(i,3)$ oraz $(i,8)$:
$\{(x,6),(y,7),(t,5),(z,?)\} \cup \{(i,8)\} =$
$\{(x,6),(y,7),(i,8),(t,5),(z,?)\}$

* Węzeł 9:
$RD_∘(9) = RD_•(4) = \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$
Przepływ przez instrukcję $[y := x]^9$:
$RD_•(9) = (RD_∘(9) \setminus \{(y,\ell) \mid \ell \in \text{Lab}\}) \cup \{(y,9)\}$
Odejmowanie usuwa $(y,2)$ oraz $(y,7)$:
$\{(x,1),(x,6),(i,3),(i,8),(t,?),(t,5),(z,?)\} \cup \{(y,9)\} =$
$\{(x,1),(x,6),(y,9),(i,3),(i,8),(t,?),(t,5),(z,?)\}$

### Zadanie 7
![](https://hackmd.io/_uploads/rJHbba4qWg.png)

### Inicjalizacja
$RD_\circ(1) = \{(x,?),\ (y,?),\ (i,?),\ (t,?),\ (z,?)\}$
Wszystkie pozostałe zbiory: $\emptyset$.

### $RD_\circ(l)$

| $l$ | iter. 0 | iter. 1 | iter. 2 |
|-----|---------|---------|---------|
| 1 | $\{(x,?),(y,?),(i,?),(t,?),(z,?)\}$ | bez zmian | bez zmian |
| 2 | $\emptyset$ | $\ \{(x,1),(y,?),(i,?),(t,?),(z,?)\}$ | bez zmian |
| 3 | $\emptyset$ | $\ \{(x,1),(y,2),(i,?),(t,?),(z,?)\}$ | bez zmian |
| 4 | $\emptyset$ | $\ \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$ |
| 5 | $\emptyset$ | $\ \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$ |
| 6 | $\emptyset$ | $\ \{(x,1),(y,2),(i,3),(t,5),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 7 | $\emptyset$ | $\ \{(x,6),(y,2),(i,3),(t,5),(z,?)\}$ | $\ \{(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 8 | $\emptyset$ | $\ \{(x,6),(y,7),(i,3),(t,5),(z,?)\}$ | $\ \{(x,6),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 9 | $\emptyset$ | $\ \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$ |

### $RD_\bullet(l)$

| $l$ | iter. 0 | iter. 1 | iter. 2 |
|-----|---------|---------|---------|
| 1 | $\emptyset$ | $\ \{(x,1),(y,?),(i,?),(t,?),(z,?)\}$ | bez zmian |
| 2 | $\emptyset$ | $\ \{(x,1),(y,2),(i,?),(t,?),(z,?)\}$ | bez zmian |
| 3 | $\emptyset$ | $\ \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$ | bez zmian |
| 4 | $\emptyset$ | $\ \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$ |
| 5 | $\emptyset$ | $\ \{(x,1),(y,2),(i,3),(t,5),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 6 | $\emptyset$ | $\ \{(x,6),(y,2),(i,3),(t,5),(z,?)\}$ | $\ \{(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 7 | $\emptyset$ | $\ \{(x,6),(y,7),(i,3),(t,5),(z,?)\}$ | $\ \{(x,6),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 8 | $\emptyset$ | $\ \{(x,6),(y,7),(i,8),(t,5),(z,?)\}$ | bez zmian |
| 9 | $\emptyset$ | $\ \{(x,1),(y,9),(i,3),(t,?),(z,?)\}$ | $\ \{(x,1),(x,6),(y,9),(i,3),(i,8),(t,?),(t,5),(z,?)\}$ |
