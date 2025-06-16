(*
Podwójna negacja znika: (¬¬p = p).
De Morgan 1: ¬(A ∧ B) = ¬A ∨ ¬B
De Morgan 2: ¬(A ∨ B) = ¬A ∧ ¬B
*)

type 'v formula =
  | Var of 'v
  | Not of 'v formula
  | And of 'v formula * 'v formula
  | Or of 'v formula * 'v formula

type 'v nnf =
  | NNFLit of bool * 'v (* true = zanegowana, false = niezanegowana *)
  | NNFDisj of 'v nnf * 'v nnf
  | NNFConj of 'v nnf * 'v nnf

let rec nnf_of_formula f =
  let rec nnf_pos f =  (* formuła w pozytywnym kontekście *)
    match f with
    | Var v -> NNFLit (false, v)
    | Not f' -> nnf_neg f'
    | And (f1, f2) -> NNFConj (nnf_pos f1, nnf_pos f2)
    | Or (f1, f2) -> NNFDisj (nnf_pos f1, nnf_pos f2)
  and nnf_neg f =  (* formuła w negatywnym kontekście *)
    match f with
    | Var v -> NNFLit (true, v)
    | Not f' -> nnf_pos f'
    | And (f1, f2) -> NNFDisj (nnf_neg f1, nnf_neg f2)
    | Or (f1, f2) -> NNFConj (nnf_neg f1, nnf_neg f2)
  in
  nnf_pos f