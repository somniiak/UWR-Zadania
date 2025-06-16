type 'a tree =
  | Leaf
  | Node of 'a tree * 'a * 'a tree;;

let rec fold_tree f a t =
  match t with
  | Leaf -> a
  | Node (l, v, r) -> f (fold_tree f a l) v (fold_tree f a r);;


let tree_product t = fold_tree (fun left v right -> left * v * right) 1 t;;
let tree_flip t = fold_tree (fun left v right -> Node (right, v, left)) Leaf t;;
let tree_height t = fold_tree (fun left _ right -> 1 + max left right) 0 t;;
let tree_span t =
  let find_min a b =
    if a < b then a else b
  in
  let find_max a b =
    if a < b then b else a
  in
  let min_val =
    fold_tree (fun left v right -> find_min (find_min left v) right) max_int t
  in
  let max_val =
    fold_tree (fun left v right -> find_max left (find_max v right)) min_int t
  in
  (min_val, max_val);;

let rec flatten t =
  match t with
  | Leaf -> []
  | Node (left, value, right) ->
      (flatten left) @ [value] @ (flatten right)