let matrix_mult m n =
  let (a, b, c, d) = m in
  let (e, f, g, h) = n in
  (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)

let matrix_id = (1, 0, 0, 1)

let matrix_expt m k =
  let rec aux t m k =
    match k with
    | 0 -> matrix_id
    | 1 -> t
    | _ -> aux (matrix_mult t m) m (k - 1)  
  in aux m m k

let fib_matrix k =
  let matrix_fib = (1, 1, 1, 0) in
  let result = (matrix_expt matrix_fib k) in
  let (_, fib_k, _, _) = result in fib_k