let matrix_mult =
  fun m n ->
    let a = fst (fst m) in
    let b = snd (fst m) in
    let c = fst (snd m) in
    let d = snd (snd m) in
    let e = fst (fst n) in
    let f = snd (fst n) in
    let g = fst (snd n) in
    let h = snd (snd n) in
    ((a * e + b * g, a * f + b * h), (c * e + d * g, c * f + d * h))
in

let matrix_expt =
  funrec matrix_expt p ->
    let m = fst p in
    let n = snd p in
    if n = 0 then
      ((1, 0), (0, 1))
    else if n = 1 then
      m
    else if n mod 2 = 0 then
      matrix_expt ((matrix_mult m m), (n / 2))
    else
      matrix_mult m (matrix_expt ((matrix_mult m m), (n / 2)))
in

let fib =
  fun n ->
    let base = ((1, 1), (1, 0)) in
    let result = matrix_expt (base, n) in
    snd (fst result)
in

fib 120