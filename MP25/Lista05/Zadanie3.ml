let list_of_string s = String . to_seq s |> List . of_seq

let parens_ok str =
  let rec aux str lpar rpar =
    match str with
    | [] -> lpar = rpar
    | '(' :: t -> aux t (lpar + 1) rpar
    | ')' :: t -> if rpar + 1 > lpar then false else aux t lpar (rpar + 1)
    | _ -> false
  in
  aux (list_of_string str) 0 0

(* Jeśli rpar + 1 > lpar w danym momencie, zwraca
  false, bo ")" nie może pojawić się przed "(". Po prostu
  każdy prawy nawias musi mieć odpowiadający mu lewy nawias*)