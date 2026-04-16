# Lista 7

### Zadanie 1
![](https://hackmd.io/_uploads/H1ja4Van-l.png)

Oczekiwane wyniki:
```
s0 = s1 + 5  = 22 + 5  = 27
s2 = s0 + s1 = 27 + 22 = 49
s3 = s0 + 15 = 27 + 15 = 42
s4 = s0 + s0 = 27 + 27 = 54
```

Rzeczywiste wyniki:
```
s0 = s1 + 5  = 27
s2 = s0 + s1 = 11 + 22 = 33
s3 = s0 + 15 = 11 + 15 = 26
s4 = s0 + s0 = 27 + 27 = 54
```

![](https://hackmd.io/_uploads/HJSEld6n-l.png)

### Zadanie 2
![](https://hackmd.io/_uploads/B1ATVNah-x.png)

**a)**
```=
s1 = s2 + 5
t0 = t1 - t2
t3 = *(s1 + 15)
*(t0 + 72) = t5
t2 = s4 & s5
```

Hazardy:
- Instr. 3: używamy `s1` z I1
- Instr. 4: używamy `t0` z I2

Oba przypadki obsługujemy forwardingiem.

![](https://hackmd.io/_uploads/Sy8CCKanZg.png)


**b)**
```=
s0 = t0 + t1
s1 = t2 - t3
s2 = s0 & s1
s3 = t4 | t5
s4 = s2 + s3
```

Hazardy:
- Instr. 3: potrzebujemy `s0` z I1 i `s1` z I2
- Instr. 5: potrzebujemy `s2` z I3 i `s3` z I4

Oba przypadki obsługujemy forwardingiem.

![](https://hackmd.io/_uploads/HJVkJ9ah-l.png)


**c)**
```=
t0 = s0 + s1
t0 = t0 - s2
t1 = *(t0 + 60)
t2 = t1 & t0
```

Hazardy:
- Instr. 2: potrzebujemy `t0` z I1
- Instr. 3: potrzebujemy `t0` z I2
- Instr. 4: potrzebujemy `t1` z I3 (instr. lw)

Pierwsze dwa przypadkie możemy rozwiązać forwardingiem. W ostatnim mamy doczynienia z instrukcją `lw` więc potrzebujemy stallingu.

![](https://hackmd.io/_uploads/Sycvzq63Zg.png)

**d)**
```=
t0 = s0 + s1
t1 = *(s2 + 60)
t2 = t0 - t3
t3 = t1 & t0
```

Hazardy:
- Instr. 3: potrzebujemy `t0` z I1
- Instr. 4: potrzebujemy `t1` z I2

Oba przypadki obsługujemy forwardingiem.

![](https://hackmd.io/_uploads/ryyfdjphbx.png)

### Zadanie 3
![](https://hackmd.io/_uploads/rJxR44p2Wg.png)

![](https://hackmd.io/_uploads/S1oeghp2bl.jpg)

### Zadanie 4
![](https://hackmd.io/_uploads/SyQ0NNp2Wx.png)

**a) always-taken**
`always-taken` - zakładamy, że instrukcja skoku zawsze się wykona. Wykonujemy instrukcje ze skoku. Jeśli się nie wykona, flushujemy.

![](https://hackmd.io/_uploads/HybuvmC3-g.png)

**b) always-not-taken**
`always-not-taken` - zakładamy, że instrukcja skoku nigdy się nie wykona. Wykonujemy instrukcje po pętli. Jeśli jednak okaże się, że instrukcja skoku zostanie wykonana, flushujemy instrukcje, które po niej były.

![](https://hackmd.io/_uploads/ByhOwQR3Wg.png)

### Zadanie 5
![](https://hackmd.io/_uploads/rkDCVNT3be.png)

**a)**
_Early branch execution_ - decyzja o skoku odbywa się w fazie `Decode` a nie `Execute`, dzięki dodatkowemu układowi porównującemu wyjścia RD1 i RD2. Dzięki temu podjęta zostaje szybsza o 1 cykl decyzja o skoku. Gdy mamy wiele iteracji może to dać dużą oszczędność.

![](https://hackmd.io/_uploads/r1qRwfRnZg.png)

**b)**
Przykład hazardu:
```
s0 = s1 + s2
if s0 != 0 goto LOOP
```

![](https://hackmd.io/_uploads/SJ72SfR2Ze.png)


### Zadanie 6
![](https://hackmd.io/_uploads/rkAMn0p2Wl.png)


Wzór ogólny:
$$\Delta\text{CPI} = \underbrace{f_\text{branch}}_{\text{ile instrukcji to skoki}} \times \underbrace{p_{miss}}_{\text{część błędnych}} \times \underbrace{\text{penalty}}_{\text{cykle za błąd}}$$


**a) Statyczny always-taken**
Ppb. poprawnej predykcji: 45%
Ppb. błędnej predykcji: 55%

$\Delta CPI_{a} = 0.25 \cdot 0.55 \cdot 1 = 0.1375$

**b) Statyczny always-not-taken**
Ppb. poprawnej predykcji: 55%
Ppb. błędnej predykcji: 45%

$\Delta CPI_{b} = 0.25 \cdot 0.45 \cdot 1 = 0.1125$

**b) Predyktor 2-bitowy**
Ppb. poprawnej predykcji: 85%
Ppb. błędnej predykcji: 15%

$\Delta CPI_{b} = 0.25 \cdot 0.15 \cdot 1 = 0.0375$

**d) Zastąpienie połowy skoków instr. arytmetycznymi**
25% skoków $\rightarrow$ 12,5% skoków i 12,5% operacji arytmetycznych.Teraz operacji arytmetycznych w programie jest łącznie 45% + 12,5% = 57,5%. Liczymy jeszcze raz poprzednie punkty z nowymi proporcjami.

<center>

| Predyktor        | $CPI$ (stare) | $CPI$ (nowe) | Przyśpieszenie |
|------------------|---------------|--------------|----------------|
| always-taken     | 1.1375        | 1.0688       | 6,4%           |
| always-not-taken | 1.1125        | 1.0563       | 5,3%           |
| 2-bitowy         | 1.0375        | 1.0188       | 1,8%           |

</center>

### Zadanie 7
![](https://hackmd.io/_uploads/SkpBtSpnWx.png)

### Zadanie 8
![](https://hackmd.io/_uploads/SJFREV6nZx.png)

### Zadanie 9
![](https://hackmd.io/_uploads/HyG1r46nWx.png)
