let alpha_num = 3
let alpha_denom = 4


(* Implementacja drzewa *)
type 'a tree = Leaf | Node of 'a tree * 'a * 'a tree

type 'a sgtree = { tree : 'a tree; size : int; max_size: int }


(* Implementacja zippera *)
type 'a path =
  | Top
  | Left of 'a path * 'a * 'a tree
  | Right of 'a tree * 'a * 'a path

type 'a zipper = 'a tree * 'a path

let go_up z =
  match z with
  | _, Top -> failwith "Wierzchołek drzewa"
  | t, Left(pth, v, r) -> (Node(t, v, r), pth)
  | t, Right(l, v, pth) -> (Node(l, v, t), pth)

let go_left z =
  match z with
  | Node(l, v, r), pth -> (l, Left(pth, v, r))
  | Leaf, _ -> failwith "Brak lewego dziecka"

let go_right z =
  match z with
  | Node(l, v, r), pth -> (r, Right(l, v, pth))
  | Leaf, _ -> failwith "Brak prawego dziecka"

let rec unzip t p =
  match p with
  | Top -> t
  | Left(pth, v, r) -> unzip (Node(t, v, r)) pth
  | Right(l, v, pth) -> unzip (Node(l, v, t)) pth


(* Operacje na drzewie *)
let rec size (tree: 'a tree) : int =
  match tree with
  | Leaf -> 0
  | Node (l, _, r) -> size l + 1 + size r

let alpha_height (n : int) : int = 
  let alpha = float_of_int alpha_num /. float_of_int alpha_denom in
  if n <= 0 then 0
  else int_of_float (floor ~-.(log (float_of_int n) /. log alpha))

let rebuild_balanced (t : 'a tree) : 'a tree =
  let rec flatten t =
    match t with
    | Leaf -> []
    | Node(l, v, r) -> (flatten l) @ [v] @ (flatten r)
  in
  let rec build e =
    (* Bierzemy pierwsze n elementów listy *)
    let rec first n xs =
      match xs, n with
      | _, 0 -> []
      | [], _ -> []
      | x :: xs, n -> x :: first (n - 1) xs
    in
    (* Usuwamy pierwsze n elementów listy *)
    let rec last n xs =
      match xs, n with
      | [], _ -> []
      | xs, 0 -> xs
      | _ :: xs, n -> last (n - 1) xs
    in
    match e with
    | [] -> Leaf
    | _ ->
      let mid = List.length e / 2 in
      let left = first mid e in
      let right = last (mid + 1) e in
      Node(build left, List.nth e mid, build right)
  in
  build (flatten t)

let empty : 'a sgtree =
  { tree = Leaf; size = 0; max_size = 0 }

let find (x : 'a) (sgt : 'a sgtree) : bool =
  let rec find s t =
    match t with
    | Leaf -> false
    | Node (l, v, r) ->
      if v = s then
        true
      else if v > s then
        find s l
      else
        find s r
  in find x sgt.tree

let insert (x : 'a) (sgt : 'a sgtree) : 'a sgtree =
  let is_balanced t =
    match t with
    | Leaf -> true
    | Node(l, _, r) ->
      let size_l = float_of_int (size l) in
      let size_r = float_of_int (size r) in
      let size_t = size_l +. 1. +. size_r in
      let alpha = float_of_int alpha_num /. float_of_int alpha_denom in
      size_l <= alpha *. size_t && size_r <= alpha *. size_t
  in
  let rec find_scapegoat z =
    match z with
    | _, Top -> z
    | t, Left(pth, v, r) ->
      let parent = Node(t, v, r) in
      if is_balanced parent then
        find_scapegoat (parent, pth)
      else z
    | t, Right(l, v, pth) ->
      let parent = Node(l, v, t) in
      if is_balanced parent then
        find_scapegoat (parent, pth)
      else z
  in
  let rec insert_without_rebuilding t x =
    match t with
    | Leaf -> Node(Leaf, x, Leaf)
    | Node(l, v, r) ->
      if x < v then
        Node(insert_without_rebuilding l x, v, r)
      else
        Node(l, v, insert_without_rebuilding r x)
  in
  let rec insert_aux t d z =
    match (fst z) with
    | Leaf ->
      if d > alpha_height sgt.size then
        (* Szukamy kozła ofiarnego, wstawiamy do niego nowe dziecko,
        przebudowywujemy poddrzewo kozła i odtwarzamy resztę drzewa. *)
        let scapegoat_tree = find_scapegoat z in
        let scapegoat_tree_with_x = insert_without_rebuilding (fst scapegoat_tree) x in
        unzip (rebuild_balanced scapegoat_tree_with_x) (snd scapegoat_tree)
      else
        insert_without_rebuilding t x
    | Node(l, v, r) ->
      if x < v then
        insert_aux t (d + 1) (go_left z)
      else if x > v then
        insert_aux t (d + 1) (go_right z)
      else
        failwith "Element istnieje"
  in
  let new_tree = insert_aux sgt.tree 0 (sgt.tree, Top) in
  {
    tree = new_tree;
    size = sgt.size + 1;
    max_size = max (sgt.size + 1) sgt.max_size;
  }

let remove (x : 'a) (sgt : 'a sgtree) : 'a sgtree =
  let rec remove_from_subtree x t =
    match t with
    | Leaf -> failwith "Elementu nie ma w drzewie"
    | Node(l, v, r) ->
      if x < v then
        Node(remove_from_subtree x l, v, r)
      else if x > v then
        Node(l, v, remove_from_subtree x r)
      else
        Leaf
  in
  let rec remove_aux x z =
    match (fst z) with
    | Leaf -> failwith "Elementu nie ma w drzewie"
    | Node(l, v, r) ->
      if x < v then
        remove_aux x (go_left z)
      else if x > v then
        remove_aux x (go_right z)
      else
        match l, r with
        | Leaf, Leaf -> unzip Leaf (snd z)
        | Leaf, _ -> unzip r (snd z)
        | _, Leaf -> unzip l (snd z)
        | _, _ ->
          let rec find_min z =
            match (fst z) with
            | Node(Leaf, v, _) -> (v, z)
            | Node(l, v, r) -> find_min (go_left z)
            | Leaf -> failwith "Przypadek niemożliwy"
          in
          let (min_val, min_zip) = find_min (go_right z) in
          let new_right = remove_from_subtree min_val (fst min_zip) in
          unzip (Node (l, min_val, new_right)) (snd z)
  in
  let new_tree = remove_aux x (sgt.tree, Top) in
  let alpha = float_of_int alpha_num /. float_of_int alpha_denom in
  if float_of_int (size new_tree) < (float_of_int sgt.max_size) *. alpha then
    {
      tree = rebuild_balanced new_tree;
      size = size new_tree;
      max_size = size new_tree;
    }
  else
    {
      tree = new_tree;
      size = sgt.size - 1;
      max_size = sgt.max_size;
    }