module type DICT = sig
  type ('a , 'b) dict
  val empty : ('a , 'b) dict
  val insert : 'a -> 'b -> ('a , 'b) dict -> ('a , 'b) dict
  val remove : 'a -> ('a , 'b) dict -> ('a , 'b) dict
  val find_opt : 'a -> ('a , 'b) dict -> 'b option
  val find : 'a -> ('a , 'b) dict -> 'b
  val to_list : ('a , 'b) dict -> (' a * 'b) list
end

module ListDict : DICT = struct
  type ('a, 'b) dict = ('a * 'b) list

  let empty = []

  let rec insert key value dict =
    match dict with
    | [] -> [(key, value)]
    | (k, v) :: rest when k = key -> (key, value) :: rest
    | pair :: rest -> pair :: insert key value rest
  
  let rec remove key dict =
    match dict with
    | [] -> []
    | (k, v) :: rest when k = key -> rest
    | pair :: rest -> pair :: remove key rest

  let rec find_opt key dict =
    match dict with
    | [] -> None
    | (k, v) :: rest when k = key -> Some v
    | _ :: rest -> find_opt key rest

  let rec find key dict =
    match dict with
    | [] -> failwith "Key not found"
    | (k, v) :: rest when k = key -> v
    | _ :: rest -> find key rest

  let to_list dict = dict
end

(**
let d : (string, int) ListDict.dict = ListDict.empty
lub
let d = ListDict.empty
let d = ListDict.insert "bajo" 5 d
let v = ListDict.find_opt "jajo" d
**)
