open RawAst

exception Type_error of
  (Lexing.position * Lexing.position) * string

type type_error = {
  pos: (Lexing.position * Lexing.position);
  msg: string
}

module Env = struct
  module StrMap = Map.Make(String)
  type t = typ StrMap.t

  let initial = StrMap.empty

  let add_var env x tp =
    StrMap.add x tp env

  let lookup_var env x =
    StrMap.find_opt x env
end

module ErrorCollector = struct
  type t = type_error list

  let empty = []

  let add_error errors pos msg =
    {pos = pos; msg = msg} :: errors

  let has_errors errors =
    errors <> []

  let string_of_error err =
    let (start_pos, end_pos) = err.pos in
    Printf.sprintf "Type error at position %d-%d: %s"
      start_pos.Lexing.pos_cnum
      end_pos.Lexing.pos_cnum
      err.msg

  let rec print_errors errors =
    match errors with
    | [] -> { data = Unit; pos = (Lexing.dummy_pos, Lexing.dummy_pos) }
    | err :: rest ->
      Printf.printf "%s\n" (string_of_error err);
      print_errors rest
end

let rec string_of_typ t =
  match t with
  | TInt -> "int"
  | TBool -> "bool"
  | TUnit -> "unit"
  | TPair(t1, t2) -> "(" ^ string_of_typ t1 ^ " * " ^ string_of_typ t2 ^ ")"
  | TArrow(t1, t2) -> string_of_typ t1 ^ " -> " ^ string_of_typ t2

let rec infer_type env (e : expr) errors : typ * ErrorCollector.t =
  match e.data with
  | Unit   -> TUnit, errors
  | Int  _ -> TInt, errors
  | Bool _ -> TBool, errors
  | Var  x ->
    begin match Env.lookup_var env x with
    | Some tp -> tp, errors
    | None ->
      let err_msg = Printf.sprintf "Unbound variable %s" x in
      let errors = ErrorCollector.add_error errors e.pos err_msg in
      TUnit, errors
    end
  | Binop((Add | Sub | Mult | Div), e1, e2) ->
    let errors = check_type env e1 TInt errors in
    let errors = check_type env e2 TInt errors in
    TInt, errors
  | Binop((And | Or), e1, e2) ->
    let errors = check_type env e1 TInt errors in
    let errors = check_type env e2 TInt errors in
    TBool, errors
  | Binop((Leq | Lt | Geq | Gt), e1, e2) ->
    let errors = check_type env e1 TInt errors in
    let errors = check_type env e2 TInt errors in
    TBool, errors
  | Binop((Eq | Neq), e1, e2) ->
    let errors = check_type env e1 TInt errors in
    let errors = check_type env e2 TInt errors in
    TBool, errors
  | If(b, e1, e2) ->
    let errors = check_type env b TBool errors in
    let tp1, errors = infer_type env e1 errors in
    let errors = check_type env e2 tp1 errors in
    tp1, errors
  | Let(x, e1, e2) ->
    let tp1, errors = infer_type env e1 errors in
    let tp2, errors = infer_type (Env.add_var env x tp1) e2 errors in
    tp2, errors
  | Pair(e1, e2) ->
    let tp1, errors = infer_type env e1 errors in
    let tp2, errors = infer_type env e2 errors in
    TPair(tp1, tp2), errors
  | App(e1, e2) ->
    let tp1, errors = infer_type env e1 errors in
    begin match tp1 with
      | TArrow(tp_arg, tp_ret) ->
        let errors = check_type env e2 tp_arg errors in
        tp_ret, errors
      | _ ->
        let err_msg = "Expected a function but got " ^ string_of_typ tp1 in
        let errors = ErrorCollector.add_error errors e1.pos err_msg in
        TUnit, errors
    end
  | Fst e ->
    let tp, errors = infer_type env e errors in
    begin match tp with
      | TPair(tp1, _) -> tp1, errors
      | _ ->
        let err_msg = "Expected a pair but got " ^ string_of_typ tp in
        let errors = ErrorCollector.add_error errors e.pos err_msg in
        TUnit, errors
    end
  | Snd e ->
    let tp, errors = infer_type env e errors in
    begin match tp with
      | TPair(_, tp2) -> tp2, errors
      | _ ->
        let err_msg = "Expected a pair but got " ^ string_of_typ tp in
        let errors = ErrorCollector.add_error errors e.pos err_msg in
        TUnit, errors
    end
  | Fun(x, tp1, e) ->
    let tp2, errors = infer_type (Env.add_var env x tp1) e errors in
    TArrow(tp1, tp2), errors
  | Funrec(f, x, tp1, tp2, e) ->
    let env = Env.add_var env x tp1 in
    let env = Env.add_var env f (TArrow(tp1, tp2)) in
    let errors = check_type env e tp2 errors in
    TArrow(tp1, tp2), errors
and check_type env e expected_tp errors =
  let actual_tp, errors = infer_type env e errors in
  if actual_tp = expected_tp then 
    errors
  else
    let err_msg = Printf.sprintf "Type mismatch: expected %s, got %s" 
                  (string_of_typ expected_tp) 
                  (string_of_typ actual_tp) in
    ErrorCollector.add_error errors e.pos err_msg

let check_program e =
  let _, errors = infer_type Env.initial e ErrorCollector.empty in
  if ErrorCollector.has_errors errors then
    begin
      errors |> List.rev |> ErrorCollector.print_errors
    end
  else
    e
