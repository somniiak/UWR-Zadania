let select xs = 
  let rec aux min left rest =
    match rest with
    | [] -> (min, List.rev left)
    | h :: t ->
      if h < min then aux h (min::left) t
      else aux min (h :: left) t
    in
    match xs with
    | [] -> failwith "Pusta lista"
    | h :: t -> aux h [] t

let rec select_sort xs =
  match xs with
  | [] -> []
  | _ ->
    let (min, rest) = select xs in
    min :: select_sort rest