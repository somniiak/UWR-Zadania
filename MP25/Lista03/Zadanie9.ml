type 'a tree =
  | Leaf
  | Node of 'a tree * 'a * 'a tree;;

let rec delete x t =
  match t with
  | Leaf -> Leaf
  | Node (l, v, r) ->
     if x < v then
      Node (delete x l, v, r)
    else if x > v then
      Node (l, v, delete x r)
    else
      match l, r with
      | Leaf, Leaf -> Leaf
      | Leaf, _ -> r
      | _, Leaf -> l
      | _, _ ->
        let rec min_tree t =
          match t with
          | Leaf -> failwith "Empty"
          | Node(Leaf, v, _) -> v
          | Node(l, _, _) -> min_tree l
        in
        let min_val = min_tree r in
        Node (l, min_val, delete min_val r)