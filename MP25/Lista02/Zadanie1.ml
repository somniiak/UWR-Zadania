let rec fib n =
  if n <= 1 then n
  else fib (n - 1) + fib (n - 2)

let fib_iter n =
  let rec aux prev curr i =
    if i = 0 then prev
    else aux curr (prev + curr) (i - 1)
  in aux 0 1 n
