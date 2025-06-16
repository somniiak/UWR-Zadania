let square = fun a -> a * a;;
let inc = fun a -> a + 1;;
let compose f g = fun x -> f(g x);;

compose square inc 5;;
(* compose square inc -> fun x -> square (inc x)
(fun x -> square (inc x)) 5 -> (square (inc 5)) -> (square 6) -> 36 *)
compose inc square 5;;
(* compose inc square -> fun x -> inc (square x)
(fun x -> inc (square x)) 5 -> (inc (square 5)) -> (inc 25) -> 26 *)