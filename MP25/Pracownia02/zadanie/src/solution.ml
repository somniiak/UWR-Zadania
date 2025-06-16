type bop =
  (* arithmetic *)
  | Add | Sub | Mult | Div
  (* logic *)
  | And | Or
  (* comparison *)
  | Eq | Neq | Leq | Lt | Geq | Gt

type ident = string

type expr =
  | Int    of int
  | Binop  of bop * expr * expr
  | Bool   of bool
  | If     of expr * expr * expr
  | Let    of ident * expr * expr
  | Var    of ident
  | Cell   of int * int
  | Unit
  | Pair   of expr * expr
  | Fst    of expr
  | Snd    of expr
  | Match  of expr * ident * ident * expr
  | IsPair of expr
  | Fun    of ident * expr
  | Funrec of ident * ident * expr
  | App    of expr * expr


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

(* Mapa do przechowywania obliczonych wartości komórek *)
module CellMap = Map.Make(struct
  type t = int * int
  let compare = compare
end)

(* Stan dla DFS *)
type cell_state = NotVisited | Visiting | Visited

let rec eval_env (env : env) (cell_values : value CellMap.t) (e : expr) : value =
  match e with
  | Int i -> VInt i
  | Bool b -> VBool b
  | Binop (op, e1, e2) ->
      eval_op op (eval_env env cell_values e1) (eval_env env cell_values e2)
  | If (b, t, e) ->
      (match eval_env env cell_values b with
        | VBool true -> eval_env env cell_values t
        | VBool false -> eval_env env cell_values e
        | _ -> failwith "type error")
  | Var x ->
     (match M.find_opt x env with
       | Some v -> v
       | None -> failwith "unknown var")
  | Let (x, e1, e2) ->
      eval_env (M.add x (eval_env env cell_values e1) env) cell_values e2
  | Pair (e1, e2) -> VPair (eval_env env cell_values e1, eval_env env cell_values e2)
  | Unit -> VUnit
  | Fst e ->
      (match eval_env env cell_values e with
        | VPair (v1, _) -> v1
        | _ -> failwith "Type error")
  | Snd e ->
      (match eval_env env cell_values e with
        | VPair (_, v2) -> v2
        | _ -> failwith "Type error")
  | Match (_e1, _x, _y, _e2) ->
      failwith "Not implemented"
  | IsPair e ->
      (match eval_env env cell_values e with
        | VPair _ -> VBool true
        | _ -> VBool false)
  | Fun (x, e) -> VClosure (x, e, env)
  | Funrec (f, x, e) -> VRecClosure (f, x, e, env)
  | App (e1, e2) ->
      let v1 = eval_env env cell_values e1 in
      let v2 = eval_env env cell_values e2 in
      (match v1 with
        | VClosure (x, body, clo_env) ->
            eval_env (M.add x v2 clo_env) cell_values body
        | VRecClosure (f, x, body, clo_env) as c ->
            eval_env (clo_env |> M.add x v2 |> M.add f c) cell_values body
        | _ -> failwith "not a function")
  | Cell (row, col) ->
      (match CellMap.find_opt (row, col) cell_values with
      | Some v -> v
      | None -> failwith "cell not evaluated")

(* Zbieranie zależności komórki *)
let rec get_deps (e : expr) : (int * int) list =
  match e with
  | Int _ | Bool _ | Unit | Var _ -> []
  | Binop (_, e1, e2) -> get_deps e1 @ get_deps e2
  | If (b, t, e) -> get_deps b @ get_deps t @ get_deps e
  | Let (_, e1, e2) -> get_deps e1 @ get_deps e2
  | Pair (e1, e2) -> get_deps e1 @ get_deps e2
  | Fst e | Snd e | IsPair e -> get_deps e
  | Match (e1, _, _, e2) -> get_deps e1 @ get_deps e2
  | Fun (_, e) | Funrec (_, _, e) -> get_deps e
  | App (e1, e2) -> get_deps e1 @ get_deps e2
  | Cell (row, col) -> [(row, col)]

(* DFS do wykrywania cykli i obliczania wartości *)
let rec dfs_eval
  (spreadsheet : expr list list) (cell_states : cell_state CellMap.t ref)
  (cell_values : value CellMap.t ref) (row : int) (col : int) : bool =

  let cell_key = (row, col) in
  (* Sprawdzanie czy komórka już została odwiedzona *)
  match CellMap.find_opt cell_key !cell_states with
  | Some Visited -> true  (* Już obliczona *)
  | Some Visiting -> false  (* Cykl *)
  | Some NotVisited | None ->
      (* Sprawdzanie czy współrzędne są prawidłowe *)
      let row_list = List.nth spreadsheet row in
      if row < 0 || col < 0 || row >= List.length spreadsheet || col >= List.length row_list then
        failwith "invalid cell coordinates"
      else
        let expr = List.nth row_list col in
        (* Oznaczenie komórki jako odwiedzona *)
        cell_states := CellMap.add cell_key Visiting !cell_states;
        (* Zebranie zależności *)
        let deps = get_deps expr in
        (* Rekurencyjnie obliczenie wszystkich zależności *)
        let deps_ok = List.for_all (
          fun (dep_row, dep_col) ->
          dfs_eval spreadsheet cell_states cell_values dep_row dep_col
        ) deps in
        if not deps_ok then false  (* Znaleziono cykl w zależnościach *)
        else
          (* Obliczanie wartość komórki *)
          try
            let value = eval_env M.empty !cell_values expr in
            cell_values := CellMap.add cell_key value !cell_values;
            cell_states := CellMap.add cell_key Visited !cell_states;
            true
          with
          | _ -> false

let eval_spreadsheet (s : expr list list) : value list list option =
  let cell_states = ref CellMap.empty in
  let cell_values = ref CellMap.empty in
  (* Próba obliczenia wszystkich komórek *)
  let rows = List.length s in
  (* Iterowanie przez wszystkie komórki *)
  let rec process_all_cells row =
    if row >= rows then true
    else
      let row_list = List.nth s row in
      let cols = List.length row_list in
      let rec process_row_cells col =
        if col >= cols then true
        else
          if dfs_eval s cell_states cell_values row col then process_row_cells (col + 1)
          else false
      in
      if process_row_cells 0 then process_all_cells (row + 1)
      else false
  in
  if process_all_cells 0 then
    (* Budowanie wynikowej listy list *)
    let result = List.mapi (fun row_idx row_list ->
      List.mapi (fun col_idx _ ->
        match CellMap.find_opt (row_idx, col_idx) !cell_values with
        | Some v -> v
        | None -> failwith "cell not evaluated"
      ) row_list
    ) s in
    Some result
  else
    None
