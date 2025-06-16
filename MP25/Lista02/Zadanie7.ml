let is_sorted xs =
  let rec aux x ys =
    match ys with
    | [] -> true
    | [h] -> if x <= h then true else false 
    | h :: t -> if x <= h then aux h t else false
  in
  match xs with
  | [] -> true
  | h :: t -> aux h t