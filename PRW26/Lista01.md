# Lista 1

### Zadanie 1
![](https://hackmd.io/_uploads/rJM1vb2sze.png)

---

**a)**
Aby dwa rdzenie wykonały algorytm w tym samym czasie, częstotliwość każdego z nich musi wynosić $f' = f/2$. Dzięki dwukrotnemu zrównolegleniu uzyskujemy tę samą wydajność. Ponieważ napięcie $V$ jest wprost proporcjonalne do $f$ otrzymujemy $V' = V/2$. Pojemność procesora dwurdzeniowego wynosi $C' = 2C$. Stąd: $$ P' = C' V'^ 2f' = 2C \cdot \frac{V^2}{4} \cdot \frac{f}{ 2}  = \frac{1}{4} C V^2 f = \frac{1}{4} P$$

---

**b)**
Chcemy teraz, żeby k-rdzeni wykonowało algorytm w tym samym czasie co jeden. Częstotliwość każdego z nich wynosi $f' = f/k$. Napięcie jest wprost proporcjonalne do częstotliwości $V' = V/k$, pojemność $k$-razy większa $C' = k \cdot C$. Zatem: $$ P' = C' V'^2 f' =  k \cdot C \cdot \frac{V^2}{k^2} \cdot \frac{f}{k} = \frac{1}{k^2} C V^2 f = \frac{1}{k^2} P$$

---

**c)**
Chcemy wykonać algorytm w czasie $T/2$. Energię elektryczną pobraną wylicza się ze wzoru $E = P \cdot T$.

- Jeden rdzeń o częstotliwości $2f$:

<center>

$C' = C; \quad V' = 2V$
$P' = C \cdot 4V^2 \cdot 2f = 8P$
$E = 8P \cdot T/2 = 4PT$

</center>

- Dwa rdzenie o częstotliwości $f$:

<center>

$C' = 2C; \quad V' = V$
$P' = 2C \cdot V^2 \cdot f = 2P$
$E = 2P \cdot T/2 = PT$

</center>

Dwa rdzenie o częstotliwości $f$ zużywają cztery razy mniej energii i pobierają cztery razy mniejszą moc niż jeden rdzeń taktowany częstotliwością $2f$.

---

**d)**
Ponieważ moc zależy od kwadratu napięcia i liniowo od częstotliwości, wzrost częstotliwości powoduje bardzo duży wzrost poboru mocy. Zamiast tego można zwiększyć liczbę rdzeni i rozdzielić między nie obliczenia. Pozwala to uzyskać większą wydajność przy mniejszym poborze mocy niż w przypadku samego zwiększania częstotliwości.

W praktyce problemy mogą stanowić:
- algorytmów nie można podzielić idealnie na niezależne działania
- na tej samej powierzchni mieści się coraz więcej tranzystorów, ale częstotliwości ich taktowania nie można zwiększyć bez przegrzewania
- rzeczywiste napięcie nie jest dokładnie liniowe


### Zadanie 2
![](https://hackmd.io/_uploads/SkOLc-hoze.png)

---

**a)**
Dla $n = 1$ możliwe wartości to **1** i **2**.
1: $o_A(0), o_B(0), z_A(1), z_B(1)$
2: $o_A(0), z_A(1), o_B(1), z_B(2)$

---

**b)**
Największa możliwa wartość końcowa to **2n**. Każda inkrementacja musi odczytać wartość zapisaną przez poprzednią inkrementację, zanim wykona swój zapis.

---

**c)**
1. `A` odczytuje 0, a jego pierwsza inkrementacja zostaje zawieszona z `tmp = 0`;
2. `B` wykonuje $n-1$ inkrementacji, tż. `value = n - 1`;
3. `A` zapisuje $z_A(1)$. Teraz `value = 1`;
4. `B` odczytuje 1, a jego $n$-ta instrukcja zostaje zawieszona z `tmp = 1`;
5. `A` wykonuje $n-1$ inkrementacji. $n - 1 \geq 1$ wykonuje conajmniej jedną, tż. `value = n` ($\geq 2$);
6. `B` zapisuje $z_B(2)$. Teraz `value = 2`;

---

**d)**
```.
> value = 1020203 (expected 2000000)
> value = 1050309 (expected 2000000)
> value = 1887400 (expected 2000000)
> value = 1059391 (expected 2000000)
> value = 1878193 (expected 2000000)
...
```

Operacje na `int` nie są atomowe. Dochodzi do przeplotu i nie otrzymujemy poprawnego wyniku. Za każdym razem, gdy jeden wątek zapisuje wartość obliczoną ze starego odczytu, ginie część pracy drugiego.


### Zadanie 3
![](https://hackmd.io/_uploads/ByKI9W2oze.png)

### Zadanie 4
![](https://hackmd.io/_uploads/SJKU9b2iMe.png)

### Zadanie 5
![](https://hackmd.io/_uploads/B1YLqZ3ozl.png)

---

**a)**
1. *Klienci są obsługiwani zgodnie z kolejnością przybycia.* -> **Bezpieczeństwo**
Złe zdarzenie: klient B zostaje obsłużony pierwszy, mimo że przyszedł po kliencie A. Własność zapewnia, że nikt nie wyprzedzi starszego.

2. *Jeśli co najmniej dwa wątki oczekują na wejsćie do sekcji krytycznej, to przynajmniej jednemu to się udaje.* -> **Żywotność**
Dobre zdarzenie: któryś z oczekujących wątków w końcu wchodzi do sekcji krytycznej.

3. *Jeśli nastąpi przerwanie, to w ciągu sekundy drukowany jest komunikat.* -> **Bezpieczeństwo**
Złe zdarzenie: nastąpiło przerwanie i minęła sekunda bez komunikatu.

4. *Jeśli nastąpi przerwanie, to drukowany jest komunikat.* -> **Żywotność**
Dobre zdarzenie: komunikat zostanie wydrukowany.

5. *Dwie rzeczy są pewnie: śmierć i podatki.* -> **Żywotność & Żywotność**
Dobre zdarzenie 1: śmierć w końcu nadejdzie.
Dobre zdarzenie 2: w końcu będziemy musieli zapłacić podatki.

6. *Nigdy nie dojdzie do sytuacji, w której każdy filozof trzyma jedną pałeczkę i czeka na drugą.* -> **Bezpieczeństwo**
Złe zdarzenie: dochodzi do takiej sytuacji, że filozof z pałeczką czeka na drugą.

7. *Każdy klient zostanie obsłużony, i to zgodnie z kolejnością przybycia.* -> **Żywotność i Bezpieczeństwo**
Dobre zdarzenie: każdy klient zostanie w końcu obsłużony.
Złe zdarzenie: nikt nie jest obsłużony przed klientem, który przybył wcześniej.

---

**b)**
- **1 i 7**: Klient `A` przybywa, potem przybywa klient `B`, a potem `B` zostaje obsłużony, mimo że `A` czeka. Od tej chwili kolejność jest naruszona, niezależnie od dalszego przebiegu.
- **3**: Następuje przerwanie w chwili `t`, mija sekunda i w czasie `t + 1` komunikat nie został wydrukowany. Późniejszy komunikat niczego nie naprawi.
- **6**: Dochodzi do momentu kiedy wszyscy filozofowie mają pałeczkę i czekają na drugą. Ten stan zostaje osiągnięty i żadne dalsze zdarzenia go nie cofną.

Dla własności żywotności taki fragment nie istnieje, ponieważ zawsze można poczekać trochę dłużej na zajście dobrego zdarzenia - własność żywotności gwarantuje, że w skończonym czasie dojdzie ono do skutku.

---

**c)**
<center>

<table>
    <tr>
        <th>Warunek</th>
        <th>Rodzaj</th>
    </tr>
    <tr>
        <td>Wzajemne wykluczanie (zad. 3, 4)</td>
        <td>bezpieczeństwo</td>
    </tr>
    <tr>
        <td>Niezakleszczenie (zad. 3)</td>
        <td>żywotność</td>
    </tr>
    <tr>
        <td>Niezagłodzenie (zad. 3)</td>
        <td>żywotność</td>
    </tr>
    <tr>
        <td>Niezagłodzenie (zad. 4)</td>
        <td>żywotność</td>
    </tr>
    <tr>
        <td>Własność producenta–konsumenta (zad. 4)</td>
        <td>bezpieczeństwo</td>
    </tr>
</table>

</center>

[Uzasadnienie1]: <> (zły stan: dwa smoki w jeziorze \(w zad. 4: Bob i smoki jednocześnie\))
[Uzasadnienie2]: <> (dobre zdarzenie: któryś smok w końcu wchodzi do jeziora)
[Uzasadnienie3]: <> (dobre zdarzenie: konkretny smok w końcu wchodzi)
[Uzasadnienie4]: <> (dobre zdarzenie: smoki jedzą kolejny raz \(nieskończenie wiele razy\))
[Uzasadnienie5]: <> (złe zdarzenia: smoki wchodzą do jeziora bez jedzenia albo Bob dokłada jedzenie, zanim poprzednie zostało zjedzone)


### Zadanie 6
![](https://hackmd.io/_uploads/rJfJDbhjze.png)

### Zadanie 7
![](https://hackmd.io/_uploads/Sy1LjZhiMl.png)

---

**a)**
Filozofowie nigdy nie rozmawiają ze sobą, co stwarza zagrożenie zakleszczenia w sytuacji, gdy każdy z nich zabierze lewy widelec i będzie czekał na prawy (lub na odwrót).

> Filozof 0 bierze pałeczkę 0.
> Filozof 1 bierze pałeczkę 1.
> Filozof 2 bierze pałeczkę 2.
> Filozof 3 bierze pałeczkę 3.
> Filozof 4 bierze pałeczkę 4.

Każdy filozof i próbuje wziąć prawą pałeczkę `(i+1) mod N`, czyli pałeczkę trzymaną przez następnego (filozof 4 chce pałeczkę 0). Wszystkie są zajęte, więc każdy czeka w `right.get()`.

Nikt nie odłoży pałeczki, bo odkłada się dopiero po zjedzeniu, a jeść można dopiero posiadając dwie.

---

**b)**
Zakleszczenie wymaga, by wszyscy `N` filozofowie zdążyli wziąć lewą pałeczkę, zanim któryś weźmie prawą. Odstęp między `left.get()` a `right.get()` to jest bardzo krótki - filozof z jedną pałeczką zaraz dostaje drugą, a momenty zgłodnienia są losowe w przedziale do 1000 ms. Jest mała szansa, że wszyscy trafią w tą sytuację.

---

**c)**
Zamiast podnosić najpier lewą, a później prawą pałeczkę, filozof ma najpierw podnieść tą z mniejszym numerem (po lewej ma `i`, po prawj `(i+1) mod N`). Wtedy jedynie filozof `N - 1` najpierw bierze prawą pałęczkę, a później lewą.

```java
    public void run() {
        Random random = new Random();
        try {
            while (true) {
                sleep(random.nextInt(THINK_MS));   // thinks
                log("is hungry");
                Fork first  = (left.id < right.id) ? left : right;
                Fork second = (left.id < right.id) ? right : left;
                first.get();
                log("took left fork " + left.id);
                sleep(DELAY_MS);
                second.get();
                log("took right fork " + right.id + " and is eating");
                sleep(random.nextInt(EAT_MS));     // eats
                first.put();
                second.put();
                log("put both forks down");
            }
        } catch (InterruptedException e) {
            return;
        }
    }
```

**Brak zakleszczenia**: Załóżmy nie wprost, że jest zakleszczenie. Wtedy istnieje taki stan, w którym każdy z filozofów ma jedną pałeczkę i chce podnieść drugą. Niech w cyklu filozof $F_1$ trzyma pałeczkę $a_1$ i czeka na $a_2 > a_1$, a $a_2$ trzyma $F_2$, który ma ją jako swoją pierwszą (niższą) pałeczkę i czeka na $a_3$. Powtarzając, dostajemy: $a_1 < a_2 < a_3 < … < a_m < a_1$, bo cykl wraca do $F_1$. To sprzeczność. Nia ma cyklu, więc zakleszczenia też nie.

---

**d)**
Kolejność odkładania pałeczek nie ma znacznia dla zakleszczenia. Zakleszczenie powstaje, gdy ktoś czeka trzymając już pałeczkę, odkładając ją nie blokuje nic. Kolejność może jedynie wpłynąć na to, kto pierwszy dostanie pałeczkę.


### Zadanie 8
![](https://hackmd.io/_uploads/SJG1wWhofg.png)

### Zadanie 9
![](https://hackmd.io/_uploads/B1Gkwb3sMx.png)

---

Z zadania 2: $\text{value} \in {2, 2n}$. Pokażmy, że osiągalna jest każda wartość przedziału $[2, 2n]$.

Niech $t \in \{0, ..., n-1\}$.

1. `A` odczytuje 0 i zawiesza pierwszą inkrementację.
2. `B` wykonuje $n−1$ inkrementacji (`value = n − 1`).
3. `A` zapisuje 1.
4. `B` odczytuje 1 i zawiesza swoją ostatnią inkrementację.
5. `A` wykonuje $n−1−t$ pełnych inkrementacji (`value = n − t`).
6. `B` zapisuje 2 (`value = 2`).
7. `A` wykonuje pozostałe $t$ inkrementacji (`value = 2 + t`).

Liczba inkrementacji każdego wątku to $n$, a wynik wynosi $2+t$, czyli dostajemy wszystkie wartości od 2 do $n+1$.

---

**c)**
```java
public class Counter {
    private long value ;               // initialized by constructor
    public Counter ( long i) {
        value = i ;
    }
    public long getAndIncrement () {   // increment , returning prior value
        return value ++;
    }
}

Counter counter = new Counter (1);     // shared by all threads
void primePrint {
    long i = 0;
    long limit = power (10, 10);
    while (i < limit) {                // loop until all numbers taken
        i = counter.getAndIncrement(); // take next untaken number
        if (isPrime (i))
            print (i);
    }
}
```

**Powtórzenia**: `getAndIncrement()` zwraca wartość odczytaną przed zwiększeniem licznika. Jeśli dwa wątki odczytają tę samą wartość, mogą oba sprawdzić tę samą liczbę.

**Pominięcia**: wątki mogą doprowadzać do przeplotu, wartość `value` może nie osiągnąć oczekiwanego `power(10, 10) - 1`.
