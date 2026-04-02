# Lista 4

### Zadanie 1
![](https://hackmd.io/_uploads/HJaBX_Zobl.png)

$$RD_\bullet(\ell) = (RD_\circ(\ell) \setminus \underbrace{\{(x, \ell') \mid \ell' \in \text{Lab}\}}_{\text{kill}_{RD}([x:=a]^\ell)}) \cup \underbrace{\{(x, \ell)\}}_{\text{gen}_{RD}([x:=a]^\ell)}$$

### Wystąpienia kill i gen

| Równanie | $\text{kill}_{RD}$ | $\text{gen}_{RD}$ |
|----------|-------------------|-------------------|
| $RD_\bullet(1)$: $[x:=0]^1$ | $\{(x,\ell') \mid \ell' \in \text{Lab}\}$ — usuwa $(x,?)$ | $\{(x,1)\}$ |
| $RD_\bullet(2)$: $[y:=1]^2$ | $\{(y,\ell') \mid \ell' \in \text{Lab}\}$ — usuwa $(y,?)$ | $\{(y,2)\}$ |
| $RD_\bullet(3)$: $[i:=1]^3$ | $\{(i,\ell') \mid \ell' \in \text{Lab}\}$ — usuwa $(i,?)$ | $\{(i,3)\}$ |
| $RD_\bullet(4)$: $[i<z]^4$ | $\emptyset$ | $\emptyset$ |
| $RD_\bullet(5)$: $[t:=x+y]^5$ | $\{(t,\ell') \mid \ell' \in \text{Lab}\}$ — usuwa $(t,?)$ i $(t,5)$ | $\{(t,5)\}$ |
| $RD_\bullet(6)$: $[x:=y]^6$ | $\{(x,\ell') \mid \ell' \in \text{Lab}\}$ — usuwa $(x,1)$ i $(x,6)$ | $\{(x,6)\}$ |
| $RD_\bullet(7)$: $[y:=t]^7$ | $\{(y,\ell') \mid \ell' \in \text{Lab}\}$ — usuwa $(y,2)$ i $(y,7)$ | $\{(y,7)\}$ |
| $RD_\bullet(8)$: $[i:=i+1]^8$ | $\{(i,\ell') \mid \ell' \in \text{Lab}\}$ — usuwa $(i,3)$ i $(i,8)$ | $\{(i,8)\}$ |
| $RD_\bullet(9)$: $[y:=x]^9$ | $\{(y,\ell') \mid \ell' \in \text{Lab}\}$ — usuwa $(y,2)$ i $(y,7)$ | $\{(y,9)\}$ |

Równania dla $RD_\circ(\ell)$ używają $∪$ (złączenie ze wszystkich poprzedników) - tu kill i gen nie występują bezpośrednio.

### Definicja kill i gen dla $\text{read}(x)$
Instrukcja $\text{read}(x)$ przypisuje do zmiennej $x$ wartość z wejścia. Jest to przypisanie, dla którego nowa wartość $x$ jest nieznana, ale $x$ zostaje zdefiniowane w etykiecie $\ell$. Zatem:

$$\text{kill}_{RD}([\text{read}(x)]^\ell) = \{(x, \ell') \mid \ell' \in \text{Lab}\}$$

czyli dokładnie tak samo jak dla $[x := a]^\ell$ — zabijamy wszystkie poprzednie definicje $x$.

$$\text{gen}_{RD}([\text{read}(x)]^\ell) = \{(x, \ell)\}$$

czyli generujemy nową definicję $x$ w etykiecie $\ell$ — dokładnie tak samo jak dla zwykłego przypisania.

$\text{read}(x)$ to przypisanie, którego wartość jest nieznana, ale wiemy że nadano jakąś wartość $x$ - kompilator wie, że po $\text{read}(x)$ zmienna $x$ ma świeżą wartość z etykiety $\ell$.

### Automatyzacja obliczeń
Mając program jako graf przepływu sterowania, obliczanie zbiorów RD można zautomatyzować algorytmem stałopunktowym:

**Dane wejściowe:** graf przepływu $(Lab, flow)$, bloki $B^\ell$, funkcje $\text{kill}_{RD}$ i $\text{gen}_{RD}$

**Inicjalizacja:**
$$RD_\circ(\ell) := \begin{cases} \{(x,?) \mid x \in FV(S)\} & \text{jeśli } \ell = \text{init}(S) \\ \emptyset & \text{wpp.} \end{cases}$$

**Iteracja:** powtarzaj aż do stabilizacji:

$$RD_\circ(\ell) := \bigcup \{ RD_\bullet(\ell') \mid (\ell', \ell) \in \text{flow}(S) \}$$
$$RD_\bullet(\ell) := (RD_\circ(\ell) \setminus \text{kill}_{RD}(B^\ell)) \cup \text{gen}_{RD}(B^\ell)$$

**Gwarancja stopu:** zbiory RD są podzbiorami skończonego zbioru $\text{Var}^\star \times \text{Lab}^\star$, więc łańcuchy rosnące są skończone (ACC) — algorytm zawsze kończy działanie, obliczając najmniejsze rozwiązanie układu równań


### Zadanie 2
![](https://hackmd.io/_uploads/S1b87Obobl.png)

Dla każdej instrukcji definiujemy `kill` i `gen`:

| Instrukcja | killRD | genRD |
|---|---|---|
| `[x := 1]` | ${(x, ℓ') : ℓ' ∈ \text{Lab}}$ | ${(x, 1)}$ |
| `[x > 0]` | $∅$ | $∅$ |
| `[y := 1]` | ${(y, ℓ') : ℓ' ∈ \text{Lab}}$ | ${(y, 3)}$ |
| `[y := -1]` | ${(y, ℓ') : ℓ' ∈ \text{Lab}}$ | ${(y, 4)}$ |
| `[z := y]` | ${(z, ℓ') : ℓ' ∈ \text{Lab}}$ | ${(z, 5)}$ |

$RD_∘(1) = \{(x,?),(y,?),(z,?)\}$
$RD_•(1) = (RD_∘(1) \setminus kill(1)) \cup gen(1)$

$RD_∘(2) = RD_•(1)$
$RD_•(2) = RD_∘(2)$

$RD_∘(3) = RD_•(2)$
$RD_•(3) = (RD_∘(3) \setminus kill(3)) \cup gen(3)$

$RD_∘(4) = RD_•(2)$
$RD_•(4) = (RD_∘(4) \setminus kill(4)) \cup gen(4)$

$RD_∘(5) = RD_•(3) \cup RD_•(4)$
$RD_•(5) = (RD_∘(5) \setminus kill(5)) \cup gen(5)$

| Iteracja 1 | Iteracja 2 |
|---|---|
| $\{(x,?),(y,?),(z,?)\}$, $\{(x,1),(y,?),(z,?)\}$ | $\{(x,?),(y,?),(z,?)\}$, $\{(x,1),(y,?),(z,?)\}$ |
| $\{(x,1),(y,?),(z,?)\}$, $\{(x,1),(y,?),(z,?)\}$ | $\{(x,1),(y,?),(z,?)\}$, $\{(x,1),(y,?),(z,?)\}$ |
| $\{(x,1),(y,?),(z,?)\}$, $\{(x,1),(y,3),(z,?)\}$ | $\{(x,1),(y,?),(z,?)\}$, $\{(x,1),(y,3),(z,?)\}$ |
| $\{(x,1),(y,?),(z,?)\}$, $\{(x,1),(y,4),(z,?)\}$ | $\{(x,1),(y,?),(z,?)\}$, $\{(x,1),(y,4),(z,?)\}$ |
| $\{(x,1),(y,3),(y,4),(z,?)\}$, $\{(x,1),(y,3),(y,4),(z,5)\}$ | $\{(x,1),(y,3),(y,4),(z,?)\}$, $\{(x,1),(y,3),(y,4),(z,5)\}$ |

W programie po wykonaniu `[x := 1]` mamy zawsze $x = 1 > 0$, więc warunek `[x > 0]` jest zawsze prawdziwy. Gałąź else z instrukcją `[y := -1]` jest nieosiągalna.

| $l$ | $RD_\circ(l)$ faktyczne | $RD_\bullet(l)$ faktyczne |
|---|---|---|
| 1 | $\{(x,?),(y,?),(z,?)\}$ | $\{(x,1),(y,?),(z,?)\}$ |
| 2 | $\{(x,1),(y,?),(z,?)\}$ | $\{(x,1),(y,?),(z,?)\}$ |
| 3 | $\{(x,1),(y,?),(z,?)\}$ | $\{(x,1),(y,3),(z,?)\}$ |
| 4 | **nieosiągalne** | **nieosiągalne** |
| 5 | $\{(x,1),(y,3),(z,?)\}$ | $\{(x,1),(y,3),(z,5)\}$ |

Jest to konsekwencja tego, że analiza RD jest nadmiarowym przybliżeniem i nie śledzi zależności między wartościami zmiennych a przepływem sterowania - traktuje obie gałęzie instrukcji if jako możliwe, niezależnie od wartości warunku. Takie podejście jest bezpieczne (nie pomija żadnej prawdziwej definicji), ale może być nieprecyzyjne.

### Zadanie 3
![](https://hackmd.io/_uploads/rJZR4ubo-x.png)

Zmienna jest żywa jeśli zostanie później użytwa w programie (zanim jej wartość zostanie nadpisania).

| l | Blok | killLV | genLV |
|---|------|--------|-------|
| 1 | `[x := 10]` | {x} | ∅ |
| 2 | `[y := 1]` | {y} | ∅ |
| 3 | `[x > 0]` | ∅ | {x} |
| 4 | `[y := y*x]` | {y} | {y, x} |
| 5 | `[x := x−1]` | {x} | {x} |
| 6 | `[z := y]` | {z} | {y} |

```
Analiza zmiennych żywych jest analizą wsteczną (backward). Dla każdego punktu
programu wyznacza zbiór zmiennych, które mogą być użyte w przyszłości przed
następnym nadpisaniem.

Blok [x := x−1] ma kill = {x} i gen = {x} (bo x pojawia się po prawej stronie).
To jest poprawne, ale warto to explicite skomentować — może wyglądać dziwnie, że
ta sama zmienna jest jednocześnie w kill i gen. Semantycznie oznacza to: „stara
wartość x jest używana (gen), a następnie nadpisywana (kill)", ale ponieważ
LV∘(5) = (LV•(5) \ {x}) ∪ {x} = LV•(5) ∪ {x}, efektem netto jest że x zawsze
trafia do LV∘(5) niezależnie od LV•(5). To zachowanie jest właściwe.
```


**Równania:**

$$\text{LV}_\bullet(\ell) = \begin{cases} \emptyset & \text{jeśli } \ell \in \text{final}(S) \\ \bigcup \{\text{LV}_\circ(\ell') \mid (\ell', \ell) \in \text{flowR}(S)\} & \text{wpp.} \end{cases}$$

$$\text{LV}_\circ(\ell) = (\text{LV}_\bullet(\ell) \setminus \text{kill}(\ell)) \cup \text{gen}(\ell)$$

```
LV•(1) = LV∘(2)
LV•(2) = LV∘(3)
LV•(3) = LV∘(4) ∪ LV∘(6)
LV•(4) = LV∘(5)
LV•(5) = LV∘(3)
LV•(6) = ∅

LV∘(1) = (LV•(1) \ {x}) ∪ ∅      = LV•(1) \ {x}
LV∘(2) = (LV•(2) \ {y}) ∪ ∅      = LV•(2) \ {y}
LV∘(3) = (LV•(3) \ ∅)  ∪ {x}     = LV•(3) ∪ {x}
LV∘(4) = (LV•(4) \ {y}) ∪ {y,x}  = LV•(4) ∪ {y,x}
LV∘(5) = (LV•(5) \ {x}) ∪ {x}    = LV•(5) ∪ {x}
LV∘(6) = (LV•(6) \ {z}) ∪ {y}    = {y}
```

### Zadanie 4
![](https://hackmd.io/_uploads/BJBLQ_-sWe.png)

Wyrażenie `e` jest dostępne w punkcie `ℓ`, jeśli na każdej ścieżce prowadzącej do `ℓ` wyrażenie `e` zostało obliczone i żadna ze zmiennych w nim występujących nie została od tego czasu zmieniona.

![](https://hackmd.io/_uploads/HJCn7-Ms-x.png)


**Funkcje kill i gen:**
$$\text{kill}_{AE}([x := a]^\ell) = \{a' \in \text{AExp}^\star \mid x \in FV(a')\}$$
$$\text{gen}_{AE}([x := a]^\ell) = \{a' \in \text{AExp}(a) \mid x \notin FV(a')\}$$
$$\text{kill}_{AE}([b]^\ell) = \emptyset, \quad \text{gen}_{AE}([b]^\ell) = \text{AExp}(b)$$

**Równania:**
$$\text{AE}_\circ(\ell) = \begin{cases} \emptyset & \text{jeśli } \ell = \text{init}(S) \\ \bigcap \{\text{AE}_\bullet(\ell') \mid (\ell', \ell) \in \text{flow}(S)\} & \text{wpp.} \end{cases}$$

$$\text{AE}_\bullet(\ell) = (\text{AE}_\circ(\ell) \setminus \text{kill}(\ell)) \cup \text{gen}(\ell)$$

**Graf przepływu:**
```
flow = {(1,2),(2,3),(3,4),(3,6),(4,5),(5,7),(6,7)}
init(S) = 1
final(S) = {7}
```

**Zbiór wyrażeń:**
$$\text{AExp} = \{a+b,\ a*b\}$$

| l | Blok | kill | gen |
|---|------|------|-----|
| 1 | `x := a+b` | {wyrażenia zawierające x} = ∅ | {a+b} |
| 2 | `z := a*b` | {wyrażenia zawierające z} = ∅ | {a*b} |
| 3 | `x > 0` | ∅ | ∅ |
| 4 | `a := 5` | {a+b, a\*b} | ∅ |
| 5 | `y := a+b` | {wyrażenia zawierające y} = ∅ | {a+b} |
| 6 | `y := a+b` | {wyrażenia zawierające y} = ∅ | {a+b} |
| 7 | `w := a+b` | {wyrażenia zawierające w} = ∅ | {a+b} |

**Układ równań:**
```
AE∘(1) = ∅
AE∘(2) = AE•(1)
AE∘(3) = AE•(2)
AE∘(4) = AE•(3)
AE∘(5) = AE•(4)
AE∘(6) = AE•(3)
AE∘(7) = AE•(5) ∩ AE•(6)

AE•(1) = (AE∘(1) \ ∅) ∪ {a+b}       = {a+b}
AE•(2) = (AE∘(2) \ ∅) ∪ {a*b}       = AE∘(2) ∪ {a*b}
AE•(3) = (AE∘(3) \ ∅) ∪ ∅           = AE∘(3)
AE•(4) = (AE∘(4) \ {a+b, a*b}) ∪ ∅  = AE∘(4) \ {a+b, a*b}
AE•(5) = (AE∘(5) \ ∅) ∪ {a+b}       = AE∘(5) ∪ {a+b}
AE•(6) = (AE∘(6) \ ∅) ∪ {a+b}       = AE∘(6) ∪ {a+b}
AE•(7) = (AE∘(7) \ ∅) ∪ {a+b}       = AE∘(7) ∪ {a+b}
```

**Algorytm stałopunktowy:**
```
AE∘(1) = ∅
AE•(1) = {a+b}

AE∘(2) = AE•(1) = {a+b}
AE•(2) = {a+b} ∪ {a*b} = {a+b, a*b}

AE∘(3) = AE•(2) = {a+b, a*b}
AE•(3) = {a+b, a*b}

AE∘(4) = AE•(3) = {a+b, a*b}
AE•(4) = {a+b, a*b} \ {a+b, a*b} = ∅

AE∘(5) = AE•(4) = ∅
AE•(5) = AE∘(5) = {a+b}

AE∘(6) = AE•(3) = {a+b, a*b}
AE•(6) = {a+b, a*b} ∪ {a+b} = {a+b, a*b}

AE∘(7) = AE•(5) ∩ AE•(6) = {a+b} ∩ {a+b, a*b} = {a+b}
AE•(7) = {a+b} ∪ {a+b} = {a+b}
```

Wszystkie wartości $AE_∘$ i $AE_•$ zależą tylko od poprzedników bez cykli (brak pętli while), więc osiągnięto punkt stały po jednej iteracji.

### Zadanie 5
![](https://hackmd.io/_uploads/HyOUmO-oZl.png)

### Zadanie 6
![](https://hackmd.io/_uploads/rkZDmuZoZe.png)

### Zadanie 7
![](https://hackmd.io/_uploads/rJCFXdbj-l.png)

![](https://hackmd.io/_uploads/SJ5CZGfjZe.png)

Łańcuch użycie-definicja dla zmiennej $x$ w etykiecie $ℓ$ to zbiór wszystkich etykiet (definicji), z których definicja $x$ może dotrzeć do tego użycia.


$$\text{UD}(x, \ell) = \begin{cases} \{\ell' \mid (x, \ell') \in \text{RD}_\circ(\ell)\} & \text{jeśli } x \in \text{gen}_{LV}(B^\ell) \\ \emptyset & \text{w przeciwnym razie} \end{cases}$$

$UD(x, ℓ)$ jest niepuste tylko wtedy, gdy $x$ jest faktycznie używane w bloku $ℓ$. Jeśli tak, to $UD(x, ℓ)$ zawiera wszystkie etykiety $ℓ'$ takie że para $(x, ℓ')$ należy do $RD_∘(ℓ)$ — czyli wszystkie definicje $x$, które mogły dotrzeć do punktu przed wykonaniem bloku $ℓ$.

**$RD_\circ(l)$**
| $l$ | iter. 1 | iter. 2 |
|-----|---------|---------|
| 1 | $\{(x,?),(y,?),(i,?),(t,?),(z,?)\}$ | bez zmian |
| 2 | $\ \{(x,1),(y,?),(i,?),(t,?),(z,?)\}$ | bez zmian |
| 3 | $\ \{(x,1),(y,2),(i,?),(t,?),(z,?)\}$ | bez zmian |
| 4 | $\ \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$ |
| 5 | $\ \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$ |
| 6 | $\ \{(x,1),(y,2),(i,3),(t,5),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 7 | $\ \{(x,6),(y,2),(i,3),(t,5),(z,?)\}$ | $\ \{(x,6),(y,2),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 8 | $\ \{(x,6),(y,7),(i,3),(t,5),(z,?)\}$ | $\ \{(x,6),(y,7),(i,3),(i,8),(t,5),(z,?)\}$ |
| 9 | $\ \{(x,1),(y,2),(i,3),(t,?),(z,?)\}$ | $\ \{(x,1),(x,6),(y,2),(y,7),(i,3),(i,8),(t,?),(t,5),(z,?)\}$ |


## 7. Obliczenie UD(x, ℓ) dla każdego bloku

Dla każdego bloku wypisuję użyte zmienne i odpowiadające im UD:

**Instrukcja 4: `[i < z]`** - użyte: `i`, `z`
```
UD(i, 4) = {3, 8}
> UD(z, 4) = {?}
```

**Instrukcja 5: `[t := x + y]`** — użyte: `x`, `y`
```
UD(x, 5) = {1, 6}    (bo (x,1),(x,6) ∈ RD∘(5))
UD(y, 5) = {2, 7}    (bo (y,2),(y,7) ∈ RD∘(5))
```

**Instrukcja 6: `[x := y]`** — użyte: `y`
```
UD(y, 6) = {2, 7}    (bo (y,2),(y,7) ∈ RD∘(6))
```

**Instrukcja 7: `[y := t]`** — użyte: `t`
```
UD(t, 7) = {5}
```

**Instrukcja 8: `[i := i + 1]`** — użyte: `i`
```
UD(i, 8) = {3, 8}    (bo (i,3),(i,8) ∈ RD∘(8))
```

**Instrukcja 9: `[y := x]`** — użyte: `x`
```
UD(x, 9) = {1, 6}    (bo (x,1),(x,6) ∈ RD∘(9))
```

Bloki ℓ=1,2,3 nie używają żadnych zmiennych po prawej stronie (przypisują stałe), więc $UD = ∅$ dla wszystkich zmiennych.


### Zadanie 8
![](https://hackmd.io/_uploads/SymYmObj-l.png)
