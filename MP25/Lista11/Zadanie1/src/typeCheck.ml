open RawAst

exception Type_error of
  (Lexing.position * Lexing.position) * string

module Env = struct
  module StrMap = Map.Make(String)
  type t = typ StrMap.t

  let initial = StrMap.empty

  let add_var env x tp =
    StrMap.add x tp env

  let lookup_var env x =
    StrMap.find_opt x env
end

let rec string_of_typ t =
  match t with
  | TInt -> "int"
  | TBool -> "bool"
  | TUnit -> "unit"
  | TPair(t1, t2) -> "(" ^ string_of_typ t1 ^ " * " ^ string_of_typ t2 ^ ")"
  | TArrow(t1, t2) -> string_of_typ t1 ^ " -> " ^ string_of_typ t2

let rec infer_type env (e : expr) : typ =
  match e.data with
  | Unit   -> TUnit
  | Int  _ -> TInt
  | Bool _ -> TBool
  | Var  x ->
    begin match Env.lookup_var env x with
    | Some tp -> tp
    | None    ->
      raise (Type_error(e.pos,
        Printf.sprintf "Unbound variable %s" x))
    end
  | Binop((Add | Sub | Mult | Div), e1, e2) ->
    begin
      try check_type env e1 TInt
      with Type_error(_, _) -> 
        raise (Type_error(e1.pos, 
                         "Expected integer for arithmetic operation, got " ^ 
                         string_of_typ (infer_type env e1)))
    end;
    begin
      try check_type env e2 TInt
      with Type_error(_, _) -> 
        raise (Type_error(e2.pos, 
                         "Expected integer for arithmetic operation, got " ^ 
                         string_of_typ (infer_type env e2)))
    end;
    TInt
  | Binop((And | Or), e1, e2) ->
    begin
      try check_type env e1 TInt
      with Type_error(_, _) -> 
        raise (Type_error(e1.pos, 
                         "Expected integer for logical operation, got " ^ 
                         string_of_typ (infer_type env e1)))
    end;
    begin
      try check_type env e2 TInt
      with Type_error(_, _) -> 
        raise (Type_error(e2.pos, 
                         "Expected integer for logical operation, got " ^ 
                         string_of_typ (infer_type env e2)))
    end;
    TBool
  | Binop((Leq | Lt | Geq | Gt), e1, e2) ->
    begin
      try check_type env e1 TInt
      with Type_error(_, _) -> 
        raise (Type_error(e1.pos, 
                         "Expected integer for comparison operation, got " ^ 
                         string_of_typ (infer_type env e1)))
    end;
    begin
      try check_type env e2 TInt
      with Type_error(_, _) -> 
        raise (Type_error(e2.pos, 
                         "Expected integer for comparison operation, got " ^ 
                         string_of_typ (infer_type env e2)))
    end;
    TBool
  | Binop((Eq | Neq), e1, e2) ->
    let tp = infer_type env e1 in
    begin
      try check_type env e2 tp
      with Type_error(_, _) -> 
        raise (Type_error(e2.pos, 
                         Printf.sprintf "Type mismatch in equality test: expected %s, got %s" 
                         (string_of_typ tp) 
                         (string_of_typ (infer_type env e2))))
    end;
    TBool
  | If(b, e1, e2) ->
    begin
      try check_type env b TBool
      with Type_error(_, _) -> 
        raise (Type_error(b.pos, 
                         "Condition in if-expression must be a boolean, got " ^ 
                         string_of_typ (infer_type env b)))
    end;
    let tp = infer_type env e1 in
    begin
      try check_type env e2 tp
      with Type_error(_, _) -> 
        raise (Type_error(e2.pos, 
                         Printf.sprintf "Type mismatch in branches of if-expression: %s and %s" 
                         (string_of_typ tp) 
                         (string_of_typ (infer_type env e2))))
    end;
    tp
  | Let(x, e1, e2) ->
    let tp1 = infer_type env e1 in
    let tp2 = infer_type (Env.add_var env x tp1) e2 in
    tp2
  | Pair(e1, e2) ->
    TPair(infer_type env e1, infer_type env e2)
  | App(e1, e2) ->
    begin match infer_type env e1 with
      | TArrow(tp2, tp1) ->
        begin
          try check_type env e2 tp2
          with Type_error(_, _) -> 
            raise (Type_error(e2.pos, 
                             Printf.sprintf "Function argument type mismatch: expected %s, got %s" 
                             (string_of_typ tp2) 
                             (string_of_typ (infer_type env e2))))
        end;
        tp1
      | tp -> raise (Type_error(e1.pos, 
                               "Expected a function but got " ^ string_of_typ tp))
    end
  | Fst e ->
    begin match infer_type env e with
      | TPair(tp1, _) -> tp1
      | tp -> raise (Type_error(e.pos, 
                               "Expected a pair but got " ^ string_of_typ tp))
    end
  | Snd e ->
    begin match infer_type env e with
      | TPair(_, tp2) -> tp2
      | tp -> raise (Type_error(e.pos, 
                               "Expected a pair but got " ^ string_of_typ tp))
    end
  | Fun(x, tp1, e) ->
    let tp2 = infer_type (Env.add_var env x tp1) e in
    TArrow(tp1, tp2)
  | Funrec(f, x, tp1, tp2, e) ->
    let env = Env.add_var env x tp1 in
    let env = Env.add_var env f (TArrow(tp1, tp2)) in
    begin
      try check_type env e tp2
      with Type_error(_, _) -> 
        raise (Type_error(e.pos, 
                         Printf.sprintf "Function body type mismatch: expected %s, got %s" 
                         (string_of_typ tp2) 
                         (string_of_typ (infer_type env e))))
    end;
    TArrow(tp1, tp2)

and check_type env e tp =
  let tp' = infer_type env e in
  if tp = tp' then ()
  else
    failwith "Type error"

let check_program e =
  let _ = infer_type Env.initial e in
  e
