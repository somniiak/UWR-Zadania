type 'a tree =
  | Leaf
  | Node of 'a tree * 'a * 'a tree

let rec insert_bst x tree =
  match tree with
  | Leaf -> Node (Leaf, x, Leaf)
  | Node (left, v, right) ->
      if x < v then
        Node (insert_bst x left, v, right)
      else
        Node (left, v, insert_bst x right)

let rec flatten t =
  match t with
  | Leaf -> []
  | Node (left, value, right) ->
      (flatten left) @ [value] @ (flatten right)

let tree_sort xs =
  let rec aux a ys =
    match ys with
    | [] -> a
    | h :: t -> aux (insert_bst h a) t
  in flatten (aux Leaf xs)