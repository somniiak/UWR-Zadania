let maximum xs =
  let rec aux x xs =
    match xs with
    | [] -> x
    | [h] -> if x > h then x else h
    | h :: t -> if x > h then aux x t else aux h t
  in
  match xs with
  | [] -> neg_infinity
  | h :: t -> aux h t