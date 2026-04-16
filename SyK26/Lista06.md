# Lista 6

### Zadanie 1
![](https://hackmd.io/_uploads/B1-vwS2jZg.png)

### Zadanie 2
![](https://hackmd.io/_uploads/ByGvDHhibg.png)

### Zadanie 3
![](https://hackmd.io/_uploads/HyeRdSnjZl.png)

![](https://hackmd.io/_uploads/BJSOOTM2Zl.png)

**a) x = \*(y+imm)**
```.!
PC(50) -> IM(250) -> max(RF(150), SE(50) -> MX(25)) -> ALU(200) -> DM(250) -> MX(25) -> RF(150) = 1075ps
```

**b) \*(x+imm) = y**
```.!
PC(50) -> IM(250) -> max(RF(150), SE(50) -> MX(25)) -> ALU(200) -> DM(250) = 900ps
```

**c) x = y binop z**
```.!
PC(50) -> IM(250) -> RF(150) -> MX(25) -> ALU(200) -> MX(25) -> RF(150) = 850ps
```

**d) if x relop y goto L**
```.!
PC(50) -> IM(250) -> max(RF(150) -> MX(25) -> ALU(200), SE(50) -> ADD(150)) -> MX(25) = 700ps
```

**e) x = y binop imm**
```.!
PC(50) -> IM(250) -> RF(150) -> MX(25) -> ALU(200) -> MX(25) -> RF(150) = 850ps
```

**f) goto L**
```.!
PC(50) -> IM(250) -> CT(50) -> MX(25) = 375ps
```

### Zadanie 4
![](https://hackmd.io/_uploads/B1CXfvVh-e.png)

|     | x = *(y + imm) | *(x + imm) = y | if x relop y goto L | x = y binop z |
| --- | -------------- | -------------- | ------------------- | ------------- |
| $T$ | 1075ps         | 900ps         | 700ps               | 850ps         |
|  %  | 269ps (25%)    | 99ps (11%)    | 84ps (12%)          | 442ps (52%)   |

Czas stały: `1075ps`
Czas zmienny: `894ps`

$$
\frac{\text{Czas}_\text{stały}}{\text{Czas}_\text{zmienny}} =
\frac{1075ps}{894ps} \approx 1.20
$$

Zyskujemy przyśpieszenie ok. 20%.

### Zadanie 5
![](https://hackmd.io/_uploads/H1Gvvr3jZx.png)

![](https://hackmd.io/_uploads/rJfcX043Wl.png)

### Zadanie 6
![](https://hackmd.io/_uploads/HkzvPSniWe.png)

### Zadanie 7
![](https://hackmd.io/_uploads/B1fPDShjWe.png)

### Zadanie 8
![](https://hackmd.io/_uploads/BkRROBnibg.png)

### Zadanie 9
![](https://hackmd.io/_uploads/HyGvDSnoZl.png)
