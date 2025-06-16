module I = Interp

(* https://k144.github.io/tools/rpn/ *)

let rec to_pn (e : Ast.expr) : string =
  match e with
  | Ast.Int n -> string_of_int n
  | Ast.Bool true -> "true"
  | Ast.Bool false -> "false"
  | Ast.Binop (op, e1, e2) ->
    let op_str =
      match op with
      | Add -> "+"  | Sub -> "-"  | Mult -> "*"
      | Div -> "/"  | And -> "&&" | Or -> "||"
      | Eq -> "=="  | Neq -> "!=" | Gt -> ">"
      | Lt -> "<"   | Geq -> ">=" | Leq -> "<="
    in op_str ^ " " ^ to_pn e1 ^ " " ^ to_pn e2
  | _ -> failwith "not implemented"

let compile (s : string) : string =
  s
  |> Interp.parse
  |> to_pn
