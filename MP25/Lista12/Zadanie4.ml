(*
  W logice intuicjonistycznej negacja ¬p reprezentowana jest jako
  typ p -> ⊥, gdzie ⊥ to pusty typ (w OCamlu np. type empty = |).
*)
type empty = | (* pusty typ *)

let pierce
  (dn : (('p -> empty ) -> empty) -> 'p) (* prawo podwójnej negacji *)
  (hyp : ('p -> empty ) -> 'p) : 'p =    (* prawo Pierce’a *)
  dn (fun np ->                          (* np : 'p -> empty *)
    let p = hyp np                       (* hyp : ('p -> empty) -> 'p *)
    in np p                              (* np : 'p -> empty, p : 'p *)
  )
