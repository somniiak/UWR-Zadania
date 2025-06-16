module I = Interp


(* Zamiana na notację polską *)
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
  s |> Interp.parse |> to_pn


(* Obliczanie z notacji polskiej*)
type token =
  | Int of int
  | Op of string

let eval_pn (tokens : token list) : int =
  let rec loop tokens stack =
    match tokens with
    | [] ->
      (match stack with
      | [Int n] -> n
      | _ -> failwith "błąd stosu 2")
    | Int n :: rest -> loop rest (Int n :: stack)
    | Op op :: rest ->
      match stack with
      | Int a :: Int b :: stack' ->
        let result =
          match op with
          | "+" -> a + b
          | "-" -> a - b
          | "*" -> a * b
          | "/" -> a / b
          | _ -> failwith "Nieznany operator"
        in
        loop rest (Int result :: stack')
      | _ -> failwith "błąd stosu 1"
  in
  loop tokens []


let parse_token s =
  match s with
  | "+" -> Op "+"
  | "-" -> Op "-"
  | "*" -> Op "*"
  | "/" -> Op "/"
  | _ ->
    match int_of_string_opt s with
    | Some n -> Int n
    | _ -> failwith "niepoprna wartość"

(* ODWRACAMY LISTE !!! *)
let tokenize (s : string) : token list =
  s |> String.split_on_char ' ' |> List.map parse_token |> List.rev

let decompile (s : string) : int =
  s |> tokenize |> eval_pn