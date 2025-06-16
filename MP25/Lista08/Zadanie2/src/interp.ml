open Ast

let parse (s : string) : expr =
  Parser.main Lexer.read (Lexing.from_string s)

module M = Map.Make(String)

type env = value M.t

and value =
  | VInt of int
  | VBool of bool
  | VUnit
  | VPair of value * value
  | VClosure of ident * expr * env
  | VRecClosure of ident * ident * expr * env

let rec show_value v =
  match v with
  | VInt n -> string_of_int n
  | VBool v -> string_of_bool v
  | VUnit -> "()"
  | VPair (v1,v2) -> "(" ^ show_value v1 ^ ", " ^ show_value v2 ^ ")"
  | VClosure _ | VRecClosure _ -> "<fun>"

let eval_op (op : bop) (val1 : value) (val2 : value) : value =
  match op, val1, val2 with
  | Add,  VInt  v1, VInt  v2 -> VInt  (v1 + v2)
  | Sub,  VInt  v1, VInt  v2 -> VInt  (v1 - v2)
  | Mult, VInt  v1, VInt  v2 -> VInt  (v1 * v2)
  | Div,  VInt  v1, VInt  v2 -> VInt  (v1 / v2)
  | And,  VBool v1, VBool v2 -> VBool (v1 && v2)
  | Or,   VBool v1, VBool v2 -> VBool (v1 || v2)
  | Leq,  VInt  v1, VInt  v2 -> VBool (v1 <= v2)
  | Lt,   VInt  v1, VInt  v2 -> VBool (v1 < v2)
  | Gt,   VInt  v1, VInt  v2 -> VBool (v1 > v2)
  | Geq,  VInt  v1, VInt  v2 -> VBool (v1 >= v2)
  | Neq,  _,        _        -> VBool (val1 <> val2)
  | Eq,   _,        _        -> VBool (val1 = val2)
  | _,    _,        _        -> failwith "type error"

let rec eval_env (env : env) (e : expr) : value =
  match e with
  | Int i -> VInt i
  | Bool b -> VBool b
  | Binop (op, e1, e2) ->
      eval_op op (eval_env env e1) (eval_env env e2)
  | If (b, t, e) ->
      (match eval_env env b with
        | VBool true -> eval_env env t
        | VBool false -> eval_env env e
        | _ -> failwith "type error")
  | Var x ->
     (match M.find_opt x env with
       | Some v -> v
       | None -> failwith "unknown var")
  | Let (x, e1, e2) ->
      eval_env (M.add x (eval_env env e1) env) e2
  | Pair (e1, e2) -> VPair (eval_env env e1, eval_env env e2)
  | Unit -> VUnit
  | Fst e ->
      (match eval_env env e with
        | VPair (v1, _) -> v1
        | _ -> failwith "Type error")
  | Snd e ->
      (match eval_env env e with
        | VPair (_, v2) -> v2
        | _ -> failwith "Type error")
  | Match (_e1, _x, _y, _e2) ->
      failwith "Not implemented"
  | IsPair e ->
      (match eval_env env e with
        | VPair _ -> VBool true
        | _ -> VBool false)
  | Fun (x, e) -> VClosure (x, e, env)
  | Funrec (f, x, e) -> VRecClosure (f, x, e, env)
  | App (e1, e2) ->
      let v1 = eval_env env e1 in
      let v2 = eval_env env e2 in
      (match v1 with
        | VClosure (x, body, clo_env) ->
            eval_env (M.add x v2 clo_env) body
        | VRecClosure (f, x, body, clo_env) as c ->
            eval_env (clo_env |> M.add x v2 |> M.add f c) body
        | _ -> failwith "not a function")

(* Zadanie 2 *)
module SM = Map.Make(String)

let rec alpha_equiv_env (env1 : string SM.t) (env2 : string SM.t) (e1 : expr) (e2 : expr) : bool =
  match e1, e2 with
  | Int n1, Int n2 -> n1 = n2
  | Bool b1, Bool b2 -> b1 = b2
  | Unit, Unit -> true
  | Var x1, Var x2 ->
    (match SM.find_opt x1 env1, SM.find_opt x2 env2 with
     | Some y1, Some y2 -> x1 = y2 && x2 = y1
     | None, None -> x1 = x2 (* wolne zmienne muszą mieć tę samą nazwę *)
     | _, _ -> false)
  | Binop(op1, l1, r1), Binop(op2, l2, r2) ->
    op1 = op2 &&
    alpha_equiv_env env1 env2 l1 l2 &&
    alpha_equiv_env env1 env2 r1 r2
  | If(b1, t1, d1), If(b2, t2, d2) ->
    alpha_equiv_env env1 env2 b1 b2 &&
    alpha_equiv_env env1 env2 t1 t2 &&
    alpha_equiv_env env1 env2 d1 d2
  | Let(x1, e1l, e1r), Let(x2, e2l, e2r) ->
    alpha_equiv_env env1 env2 e1l e2l &&
    let new_env1 = SM.add x1 x2 env1 in
    let new_env2 = SM.add x2 x1 env2 in
    alpha_equiv_env new_env1 new_env2 e1r e2r
  | Fun(x1, d1), Fun(x2, d2) ->
    alpha_equiv_env env1 env2 d1 d2 &&
    let new_env1 = SM.add x1 x2 env1 in
    let new_env2 = SM.add x2 x1 env2 in
    alpha_equiv_env new_env1 new_env2 d1 d2
  | App(l1, r1), App(l2, r2) ->
    alpha_equiv_env env1 env2 l1 l2 &&
    alpha_equiv_env env1 env2 r1 r2
  | Pair(l1, r1), Pair(l2, r2) ->
    alpha_equiv_env env1 env2 l1 l2 &&
    alpha_equiv_env env1 env2 r1 r2
  | Fst d1, Fst d2 ->
    alpha_equiv_env env1 env2 d1 d2
  | Snd d1, Snd d2 ->
    alpha_equiv_env env1 env2 d1 d2
  | IsPair d1, IsPair d2 ->
    alpha_equiv_env env1 env2 d1 d2
  | Match(c1, x1, y1, d1), Match(c2, x2, y2, d2) ->
    alpha_equiv_env env1 env2 c1 c2 &&
    let new_env1 = SM.add y1 y2 (SM.add x1 x2 env1) in
    let new_env2 = SM.add y2 y1 (SM.add x2 x1 env2) in
    alpha_equiv_env new_env1 new_env2 d1 d2
  | Funrec(f1, x1, d1), Funrec(f2, x2, d2) ->
    let new_env1 = SM.add x1 x2 (SM.add f1 f2 env1) in
    let new_env2 = SM.add x2 x1 (SM.add f2 f1 env2) in
    alpha_equiv_env new_env1 new_env2 d1 d2
  | _, _ -> false

let alpha_equiv (e1 : expr) (e2 : expr) : bool =
  alpha_equiv_env SM.empty SM.empty e1 e2

(*
alpha_equiv
  (parse "let x = 2 in let y = 5 in x + y")
  (parse "let y = 2 in let z = 5 in y + z");;

alpha_equiv
  (parse "let x = 2 in x + y")
  (parse "let z = 2 in z + y");;

alpha_equiv
  (parse "let x = 2 in let y = 5 in x + y")
  (parse "let y = 2 in let y = 5 in y + y");;

alpha_equiv
  (parse "let x = 2 in x + y")
  (parse "let y = 2 in y + y");;
*)

let eval = eval_env M.empty

let interp (s : string) : value =
  eval (parse s)
