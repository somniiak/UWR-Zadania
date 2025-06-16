(* Wersja na bazie fold_left*)

let fold_left f a xs =
  let rec it xs acc =
    match xs with
    | [] -> acc
    | x::xs -> it xs (f acc x)
  in it xs a;;

let product = fold_left (fun acc x -> acc * x) 1;;


(* Wersja niezależna*)

let product xs =
  let rec it xs acc =
    match xs with
    | [] -> acc
    | x::xs -> it xs (acc * x)
  in it xs 1;;