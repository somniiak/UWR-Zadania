let list_of_string s = String . to_seq s |> List . of_seq

let parens_ok str =
  let rec aux str lpar rpar lsqr rsqr lcur rcur =
    match str with
    | [] -> lpar = rpar && lsqr = rsqr && lcur = rcur
    | '(' :: t -> aux t (lpar + 1) rpar lsqr rsqr lcur rcur
    | ')' :: t -> if rpar + 1 > lpar then false else aux t lpar (rpar + 1) lsqr rsqr lcur rcur
    | '[' :: t -> aux t lpar rpar (lsqr + 1) rsqr lcur rcur
    | ']' :: t -> if rsqr + 1 > lsqr then false else aux t lpar rpar lsqr (rsqr + 1) lcur rcur
    | '{' :: t -> aux t lpar rpar lsqr rsqr (lcur + 1) rcur
    | '}' :: t -> if rcur + 1 > lcur then false else aux t lpar rpar lsqr rsqr lcur (rcur + 1)
    | _ -> false
  in
  aux (list_of_string str) 0 0 0 0 0 0
