open Syntax

module TermVarSet = Set.Make(String)
module ProofVarMap = Map.Make(String)

type term_env = TermVarSet.t
type proof_env = formula ProofVarMap.t

(* Funkcja sprawdzająca dobre sformowanie termów *)
let rec check_wft (pos : position) (delta : term_env) (t : term) : unit =
  match t with
  | Var x ->
    if not (TermVarSet.mem x delta) then
      raise (Type_error (pos, "Niezwiązana zmienna termowa: " ^ x))
  | Func (_, args) ->
    List.iter (check_wft pos delta) args

(* Funkcja sprawdzająca dobre sformowanie formuł *)
let rec check_wff (pos : position) (delta : term_env) (f : formula) : unit =
  match f with
  | False -> ()
  | Rel (_, args) ->
    List.iter (check_wft pos delta) args
  | Imp (f1, f2) | And (f1, f2) | Or (f1, f2) ->
    check_wff pos delta f1;
    check_wff pos delta f2
  | Forall (x, f) | Exists (x, f) ->
    let delta' = TermVarSet.add x delta in
    check_wff pos delta' f
  | ForallRel (_, f) ->
    check_wff pos delta f

(* Funkcja sprawdzająca typowanie dowodów *)
let rec check_expr (delta : term_env) (gamma : proof_env) (e : expr) (expected_type : formula) : unit =
  match e.data with
  | EVar x ->
    (match ProofVarMap.find_opt x gamma with
      | Some phi ->
        if not (Formula.equal phi expected_type) then
          raise (Type_error (e.pos, "Niezgodność typów dla zmiennej " ^ x))
      | None ->
        raise (Type_error (e.pos, "Niezwiązana zmienna dowodowa " ^ x)))
  | ELet (x, e1, e2) ->
    let phi = infer_expr delta gamma e1 in
    let gamma' = ProofVarMap.add x phi gamma in
    check_expr delta gamma' e2 expected_type
  | EFun (x, phi, e_body) ->
    (match expected_type with
      | Imp (phi', psi) ->
        if not (Formula.equal phi phi') then
          raise (Type_error (e.pos, "Niezgodność typu implikacji"));
        check_wff e.pos delta phi;
        let gamma' = ProofVarMap.add x phi gamma in
        check_expr delta gamma' e_body psi
      | _ ->
        raise (Type_error (e.pos, "Oczekiwano typu implikacji")))
  | EApp (e1, e2) ->
    let phi_to_psi = infer_expr delta gamma e1 in
    (match phi_to_psi with
      | Imp (phi, psi) ->
        check_expr delta gamma e2 phi;
        if not (Formula.equal psi expected_type) then
          raise (Type_error (e.pos, "Niezgodność typu wyniku aplikacji"))
      | _ ->
        raise (Type_error (e.pos, "Nie można zastosować obiektu, który nie jest funkcją")))
  | ETermFun (x, e_body) ->
    (match expected_type with
      | Forall (y, phi) ->
        if TermVarSet.mem x delta then
          raise (Type_error (e.pos, "Zmienna termowa " ^ x ^ " już jest związana"));
        let delta' = TermVarSet.add x delta in
        let phi_subst = Formula.subst y (Var x) phi in
        check_expr delta' gamma e_body phi_subst
      | _ ->
        raise (Type_error (e.pos, "Oczekiwano typu z kwantyfikatorem uniwersalnym do funkcji")))
  | ETermApp (e1, t) ->
    let forall_phi = infer_expr delta gamma e1 in
    (match forall_phi with
      | Forall (x, phi) ->
        check_wft e.pos delta t;
        let result_type = Formula.subst x t phi in
        if not (Formula.equal result_type expected_type) then
          raise (Type_error (e.pos, "Niezgodność typu po podstawieniu termu"))
      | _ ->
        raise (Type_error (e.pos, "Nie można zastosować termu do nie-kwantyfikatora")))    
  | ERelApp (e1, x, psi) ->
    let forall_rel_phi = infer_expr delta gamma e1 in
    (match forall_rel_phi with
      | ForallRel (r, phi) ->
        let delta' = TermVarSet.add x delta in
        check_wff e.pos delta' psi;
        let result_type = Formula.subst_rel r (x, psi) phi in
        if not (Formula.equal result_type expected_type) then
          raise (Type_error (e.pos, "Niezgodność typu po podstawieniu relacji"))
      | _ ->
        raise (Type_error (e.pos, "Nie można zastosować relacji bez kwantyfikatora drugiego rzędu")))
  | EPair (e1, e2) ->
    (match expected_type with
      | And (phi, psi) ->
        check_expr delta gamma e1 phi;
        check_expr delta gamma e2 psi
      | _ ->
        raise (Type_error (e.pos, "Oczekiwano typu koniunkcji dla pary")))    
  | EFst e1 ->
    let phi_and_psi = infer_expr delta gamma e1 in
      (match phi_and_psi with
      | And (phi, _) ->
        if not (Formula.equal phi expected_type) then
          raise (Type_error (e.pos, "Niezgodność typu pierwszego elementu"))
      | _ ->
        raise (Type_error (e.pos, "Nie można pobrać pierwszego elementu")))
  | ESnd e1 ->
    let phi_and_psi = infer_expr delta gamma e1 in
    (match phi_and_psi with
      | And (_, psi) ->
        if not (Formula.equal psi expected_type) then
          raise (Type_error (e.pos, "Niezgodność typu drugiego elementu"))
      | _ ->
        raise (Type_error (e.pos, "Nie można pobrać drugiego elementu")))
  | ELeft (e1, phi_or_psi) ->
    (match phi_or_psi with
      | Or (phi, _) ->
        if not (Formula.equal phi_or_psi expected_type) then
          raise (Type_error (e.pos, "Niezgodność typu lewej alternatywy"));
        check_wff e.pos delta phi_or_psi;
        check_expr delta gamma e1 phi
      | _ ->
        raise (Type_error (e.pos, "Lewa strona wymaga typu alternatywy")))
  | ERight (e1, phi_or_psi) ->
      (match phi_or_psi with
      | Or (_, psi) ->
        if not (Formula.equal phi_or_psi expected_type) then
          raise (Type_error (e.pos, "Niezgodność typu prawej alternatywy"));
        check_wff e.pos delta phi_or_psi;
        check_expr delta gamma e1 psi
      | _ ->
        raise (Type_error (e.pos, "Prawa strona wymaga typu alternatywy")))
  | ECase (e0, x, e1, y, e2) ->
    let phi_or_psi = infer_expr delta gamma e0 in
    (match phi_or_psi with
      | Or (phi, psi) ->
        let gamma1 = ProofVarMap.add x phi gamma in
        let gamma2 = ProofVarMap.add y psi gamma in
        check_expr delta gamma1 e1 expected_type;
        check_expr delta gamma2 e2 expected_type
      | _ ->
        raise (Type_error (e.pos, "Analiza przypadków wymaga alternatywy")))
  | EAbsurd (e1, phi) ->
    let false_type = infer_expr delta gamma e1 in
      (match false_type with
        | False ->
          if not (Formula.equal phi expected_type) then
            raise (Type_error (e.pos, "Niezgodność typu w eliminacji sprzeczności"));
          check_wff e.pos delta phi
        | _ ->
          raise (Type_error (e.pos, "Eliminacja sprzeczności wymaga typu False")))
  | EPack (t, e1, exists_phi) ->
    (match exists_phi with
      | Exists (x, phi) ->
        if not (Formula.equal exists_phi expected_type) then
          raise (Type_error (e.pos, "Niezgodność typu w pack"));
        check_wft e.pos delta t;
        check_wff e.pos delta exists_phi;
        let phi_subst = Formula.subst x t phi in
        check_expr delta gamma e1 phi_subst
      | _ ->
        raise (Type_error (e.pos, "Pack wymaga kwantyfikatora egzystencjalnego")))
  | EUnpack (x, y, e1, e2) ->
    let exists_phi = infer_expr delta gamma e1 in
    (match exists_phi with
      | Exists (z, phi) ->
        if TermVarSet.mem x delta then
          raise (Type_error (e.pos, "Zmienna termowa " ^ x ^ " już jest związana"));
        if Formula.contains_tvar x expected_type then
          raise (Type_error (e.pos, "Zmienna termowa " ^ x ^ " ucieka ze swojego zakresu"));
        let delta' = TermVarSet.add x delta in
        let phi_renamed = Formula.subst z (Var x) phi in
        let gamma' = ProofVarMap.add y phi_renamed gamma in
        check_wff e.pos delta expected_type;
        check_expr delta' gamma' e2 expected_type
      | _ ->
        raise (Type_error (e.pos, "Unpack wymaga kwantyfikatora egzystencjalnego")))

(* Inferencja typów *)
and infer_expr (delta : term_env) (gamma : proof_env) (e : expr) : formula =
  match e.data with
  | EVar x ->
    (match ProofVarMap.find_opt x gamma with
      | Some phi -> phi
      | None -> raise (Type_error (e.pos, "Niezwiązana zmienna dowodowa: " ^ x)))    
  | ELet (x, e1, e2) ->
    let phi = infer_expr delta gamma e1 in
    let gamma' = ProofVarMap.add x phi gamma in
    infer_expr delta gamma' e2
  | EFun (x, phi, e_body) ->
    check_wff e.pos delta phi;
    let gamma' = ProofVarMap.add x phi gamma in
    let psi = infer_expr delta gamma' e_body in
    Imp (phi, psi)
  | EApp (e1, e2) ->
    let phi_to_psi = infer_expr delta gamma e1 in
    (match phi_to_psi with
      | Imp (phi, psi) ->
        check_expr delta gamma e2 phi;
        psi
      | _ ->
        raise (Type_error (e.pos, "Nie można zastosować obiektu, który nie jest funkcją")))
  | ETermFun (x, e_body) ->
    if TermVarSet.mem x delta then
      raise (Type_error (e.pos, "Zmienna termowa " ^ x ^ " już jest związana"));
    let delta' = TermVarSet.add x delta in
    let phi = infer_expr delta' gamma e_body in
    Forall (x, phi)
  | ETermApp (e1, t) ->
    let forall_phi = infer_expr delta gamma e1 in
    (match forall_phi with
      | Forall (x, phi) ->
        check_wft e.pos delta t;
        Formula.subst x t phi
      | _ ->
        raise (Type_error (e.pos, "Oczekiwano typu z kwantyfikatorem uniwersalnym")))    
  | ERelApp (e1, x, psi) ->
    let forall_rel_phi = infer_expr delta gamma e1 in
    (match forall_rel_phi with
      | ForallRel (r, phi) ->
        let delta' = TermVarSet.add x delta in
        check_wff e.pos delta' psi;
        Formula.subst_rel r (x, psi) phi
      | _ ->
        raise (Type_error (e.pos, "Nie można zastosować relacji bez kwantyfikatora drugiego rzędu")))
  | EPair (e1, e2) ->
    let phi = infer_expr delta gamma e1 in
    let psi = infer_expr delta gamma e2 in
    And (phi, psi)
  | EFst e1 ->
    let phi_and_psi = infer_expr delta gamma e1 in
      (match phi_and_psi with
      | And (phi, _) -> phi
      | _ -> raise (Type_error (e.pos, "Nie można pobrać pierwszego elementu")))
  | ESnd e1 ->
    let phi_and_psi = infer_expr delta gamma e1 in
      (match phi_and_psi with
      | And (_, psi) -> psi
      | _ -> raise (Type_error (e.pos, "Nie można pobrać drugiego elementu")))
  | ELeft (e1, phi_or_psi) ->
    (match phi_or_psi with
      | Or (phi, _) ->
        check_wff e.pos delta phi_or_psi;
        check_expr delta gamma e1 phi;
        phi_or_psi
      | _ ->
        raise (Type_error (e.pos, "Lewa strona wymaga typu alternatywy")))
  | ERight (e1, phi_or_psi) ->
    (match phi_or_psi with
      | Or (_, psi) ->
        check_wff e.pos delta phi_or_psi;
        check_expr delta gamma e1 psi;
        phi_or_psi
      | _ ->
        raise (Type_error (e.pos, "Prawa strona wymaga typu alternatywy")))
  | ECase (e0, x, e1, y, e2) ->
    let phi_or_psi = infer_expr delta gamma e0 in
    (match phi_or_psi with
      | Or (phi, psi) ->
        let gamma1 = ProofVarMap.add x phi gamma in
        let gamma2 = ProofVarMap.add y psi gamma in
        let result1 = infer_expr delta gamma1 e1 in
        let result2 = infer_expr delta gamma2 e2 in
        if not (Formula.equal result1 result2) then
          raise (Type_error (e.pos, "Strony przypadków mają różne typy"));
        result1
      | _ ->
        raise (Type_error (e.pos, "Analiza przypadków wymaga alternatywy")))
  | EAbsurd (e1, phi) ->
    let false_type = infer_expr delta gamma e1 in
    (match false_type with
      | False ->
        check_wff e.pos delta phi;
        phi
      | _ ->
        raise (Type_error (e.pos, "Eliminacja sprzeczności wymaga typu False")))
  | EPack (t, e1, exists_phi) ->
    (match exists_phi with
      | Exists (x, phi) ->
        check_wft e.pos delta t;
        check_wff e.pos delta exists_phi;
        let phi_subst = Formula.subst x t phi in
        check_expr delta gamma e1 phi_subst;
        exists_phi
      | _ ->
        raise (Type_error (e.pos, "Pack wymaga kwantyfikatora egzystencjalnego")))
  | EUnpack (x, y, e1, e2) ->
    let exists_phi = infer_expr delta gamma e1 in
    (match exists_phi with
      | Exists (z, phi) ->
        if TermVarSet.mem x delta then
          raise (Type_error (e.pos, "Zmienna termowa " ^ x ^ " już jest związana"));
        let delta' = TermVarSet.add x delta in
        let phi_renamed = Formula.subst z (Var x) phi in
        let gamma' = ProofVarMap.add y phi_renamed gamma in
        let result = infer_expr delta' gamma' e2 in
        if Formula.contains_tvar x result then
          raise (Type_error (e.pos, "Zmienna termowa " ^ x ^ " ucieka ze swojego zakresu"));
        result
      | _ ->
        raise (Type_error (e.pos, "Unpack wymaga kwantyfikatora egzystencjalnego")))

(* Funkcja sprawdzająca pojedynczą definicję *)
let check_def (gamma : proof_env) (def : def) : proof_env =
  match def with
  | Axiom (pos, x, phi) ->
    check_wff pos TermVarSet.empty phi;
    ProofVarMap.add x phi gamma
  | Theorem (pos, x, phi, e) ->
    check_wff pos TermVarSet.empty phi;
    check_expr TermVarSet.empty gamma e phi;
    ProofVarMap.add x phi gamma

let check_defs (defs : def list) : unit =
  let rec loop gamma defs =
    match defs with
    | [] -> ()
    | def :: rest ->
      let gamma' = check_def gamma def in
      loop gamma' rest
  in
  loop ProofVarMap.empty defs