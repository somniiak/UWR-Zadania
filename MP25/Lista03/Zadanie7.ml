type 'a tree =
  | Leaf
  | Node of 'a tree * 'a * 'a tree

let rec flat_append t xs =
  match t with
  | Leaf -> xs
  | Node (left, v, right) -> flat_append left (v :: flat_append right xs)

let flatten t = flat_append t []