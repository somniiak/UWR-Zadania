let rec mem x xs =
  match xs with
  | [] -> false
  | h :: t -> h = x || mem x t
