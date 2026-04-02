# Lista 5

### Zadanie 1
![](https://hackmd.io/_uploads/r1TaSdBsZg.png)

### Zadanie 2
![](https://hackmd.io/_uploads/BJKX_uro-l.png)

### Zadanie 3
![](https://hackmd.io/_uploads/H1XRHOSjbe.png)

1. **while(b) {...}**
```.
LOOP:
      if (b == false) goto END
      ...
      goto LOOP
END:
```

2. **for(i = 0; i < n; i++) {...}**
```.
      i := 0
LOOP:
      if(i >= n) goto END
      ...
      i := i + 1
      goto LOOP
END:
```

3. **do {...} while (b)**
```.
LOOP:
      ...
      if (b == true) goto LOOP
```

### Zadanie 4
![](https://hackmd.io/_uploads/SkHQ_uSiZg.png)

**Część 1**
```.
t1 := a * a
t2 := b * b

t3 := t1 * a  // a^3
t1 := t1 * 4  // 4*a^2
t1 := t1 * b  // 4*a^2*b
t1 := t1 + t3 // a^3 + 4*a^2*b

t4 := t2 * b  // b^3
t5 := t2 * 4  // 4*b^2
t5 := t5 * a  // 4*a*b^2
t5 := t5 + t4 // b^3 4*a*b^2

x := t1 + t5
```

**Część 2**
```.
t1 := a * a
t2 := t1 * a
*mem := t2        // mem[0] = a^3

t2 := 4 * t1
t2 := t2 * b      // t2 = 4*a^2*b
t1 := *mem        // t1 = a^3
t1 := t1 + t2     // t1 = a^3 + 4*a^2*b
*mem := t1        // mem[0] = a^3 + 4*a^2*b

t1 := b * b       // t1 = b^2
t2 := 4 * t1
t2 := t2 * a      // t2 = 4*a*b^2

t1 := t1 * b      // t1 = b^3
t1 := t1 + t2     // t1 = 4*a*b^2 + b^3

t2 := *mem        // t2 = a^3 + 4*a^2*b
x := t1 + t2
```

### Zadanie 5
![](https://hackmd.io/_uploads/BkRRHdBj-g.png)

**Bubble sort**
```c
for (i = 0; i < n - 1; i++) {
    for (j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
            temp = a[j];
            a[j] = a[j + 1];
            a[j + 1] = temp;
        }
    }
}
```

**Kod trójkowy**
```.
; dane: tablica bajtów pod adresem arr, rozmiar n
; rejestry: i, j, t1, t2, t3

        i := 0
loop_i:
        t1 := n - 1
        if i >= t1 goto end

        j := 0
loop_j:
        t1 := n - 1
        t1 := t1 - i
        if j >= t1 goto next_i

        t1 := arr + j
        t2 := *t1         ; t2 = arr[j]
        t1 := arr + j + 1
        t3 := *t1         ; t3 = arr[j+1]
        if t2 <= t3 goto no_swap

        t1 := arr + j
        *t1 := t3         ; arr[j] = arr[j+1]
        t1 := arr + j + 1
        *t1 := t2         ; arr[j+1] = arr[j]

no_swap:
        j := j + 1
        goto loop_j

next_i:
        i := i + 1
        goto loop_i

end:
```

### Zadanie 6
![](https://hackmd.io/_uploads/rkKkUOHiZe.png)

![](https://hackmd.io/_uploads/BkyH3Hjsbe.png)


### Zadanie 7
![](https://hackmd.io/_uploads/SJh1IOSjWg.png)

![](https://hackmd.io/_uploads/rkt38IsjWg.png)


### Zadanie 8
![](https://hackmd.io/_uploads/ByxeIdHobl.png)

![](https://hackmd.io/_uploads/rJeTQwoibl.png)
