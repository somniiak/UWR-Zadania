type bop =
  (* arithmetic *)
  | Add | Sub | Mult | Div
  (* logic *)
  | And | Or
  (* comparison *)
  | Eq | Leq

type ident = string

type expr = 
  | Int       of int
  | Binop     of bop * expr * expr
  | Bool      of bool
  | If        of expr * expr * expr
  | Let       of ident * expr * expr
  | Var       of ident
  | ForLoop   of ident * expr * expr * expr  (* for i := n to m do body end *)
  | Integral  of ident * expr * expr * expr  (* całka oznaczona ∫_n^m f(x) dx *)

(*
ForLoop reprezentuje pętlę for w stylu Pascala:
-pierwszy argument to identyfikator (nazwa zmiennej iteracyjnej)
-drugi argument określa początek zakresu (n)
-trzeci argument określa koniec zakresu (m)
-czwarty argument to ciało pętli

Integral reprezentuje całkę oznaczoną:
-pierwszy argument to zmienna całkowania
-drugi argument to dolna granica całkowania
-trzeci argument to górna granica całkowania
-czwarty argument to całkowana funkcja
*)