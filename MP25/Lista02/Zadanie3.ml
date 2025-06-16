let matrix_mult m n =
  let (a, b, c, d) = m in
  let (e, f, g, h) = n in
  (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)

let matrix_id = (1, 0, 0, 1)

let rec matrix_expt_fast m k =
  match k with
  | 0 -> matrix_id
  | 1 -> m
  | _ -> if k mod 2 = 0
    then (matrix_expt_fast (matrix_mult m m) (k / 2))
    else (matrix_mult m (matrix_expt_fast (matrix_mult m m) (k / 2)))

let fib_fast k =
  let matrix_fib = (1, 1, 1, 0) in
  let result = (matrix_expt_fast matrix_fib k) in
  let (_, fib_k, _, _) = result in fib_k