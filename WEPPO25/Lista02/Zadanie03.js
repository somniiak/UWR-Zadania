console.log( (![]+[])[+[]]+(![]+[])[+!+[]]+([![]]+[][[]])[+!+[]+[+[]]]+(![]+[])[!+[]+!+[]] );

let group1 = ![]+[] // [] jest traktowane jakoby miało wartość true, ![] -> false, false + [] -> "false"
group1 = group1[+[]] // +[] jest zamieniane na 0, i próbuje się odwołać do pierwszego elementu tablicy "false" -> 'f'
console.log(group1)

let group2 = (![]+[]) // Tak samo jak poprzednio
//console.log(+!+[]) // [] -> 0, !+[] -> !0 -> !false -> true, +true -> 1
group2 = group2[+!+[]] // "false"[1] -> 'a'
console.log(group2)

let group3 = [![]] // [ false ]
group3 = group3 + [][[]] // szukamy własności [] -> "" w pustej tablicy -> undefined; Wynik: falseundefined
// console.log(+!+[]+[+[]]) // +[] -> 0, !0 -> true, +true -> 1; [+[]] -> [0]; 1 + [0] -> "1" + "0" -> "10"
group3 = group3[+!+[]+[+[]]]
console.log(group3)

let group4 = ![]+[] // Tak jak poprzednio
group4 = group4[!+[]+!+[]] // +[] -> 0, !0 -> true, true + true -> 2, "false"[2] -> 'l'
console.log(group4)