let split xs =
  let rec aux xs (left, right) =
    match xs with
    | [] -> (left, right)
    | [h] -> aux [] (h :: left, right)
    | h :: n :: t ->
      aux t (h :: left, n :: right)
  in
  match xs with
  | [] -> failwith "Pusta lista"
  | _ -> aux xs ([], [])

let merge xs ys =
  let rec aux res ls rs =
    match ls, rs with
    | [], [] -> List.rev res
    | [], h :: tr -> aux (h :: res) [] tr
    | h :: tl, [] -> aux (h :: res) tl []
    | hl :: tl, hr :: tr ->
      if hl < hr then aux (hl :: res) tl rs
      else aux (hr :: res) ls tr
  in
  match xs, ys with
  | _, [] | [], _ -> failwith "Pusta lista"
  | _, _ -> aux [] xs ys

let rec merge_sort xs =
  match xs with
  | [h] -> xs
  | [l; r] -> if l < r then [l; r] else [r; l]
  | _ ->
      let left, right = split xs in
      merge (merge_sort left) (merge_sort right)