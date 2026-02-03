/*
Zmienna `var` jest dostępna w całym ciele funkcji w której została
zdefiniowana, niezależnie od zagnieżdżenia. Zmienna `let` jest
dostępna tylko w tym samym bloku, w którym została zdefiniowana.

Wszystkie funkcje zwracają 10, bo zmienna `i` zadeklarowana przez
`var` ma zasięg funkcyjny, a nie blokowy. Po zakończeniu pętli for,
wartość `i` wynosi 10, więc każda funkcja w tablicy odwołuje się
do tej samej zmiennej `i`, która już ma wartość końcową.

`let` ma zasięg blokowy, więc w każdej iteracji pętli for
powstaje nowa, odrębna zmienna i.

W rozwiązaniu używającym samego `var` tworzymy pomocniczą funkcję
`loop` która przyjmuje `i` jako argument żeby zapisać obecne `i`
w zwracanej funkcji.

function createFs(n) {
    var fs = [];

    var _loop = function _loop(i) {
        fs[i] = function () {
            return i;
        };
    };

    for (var i = 0; i < n; i++) {
      _loop(i);
    };

    return fs;
}
*/

function createFs(n) {
    var fs = [];

    for (let i = 0; i < n; i++)
        fs[i] = _ => i

    return fs;
}

var myfs = createFs(10);

console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());