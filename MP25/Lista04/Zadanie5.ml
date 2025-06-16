module type KDICT = sig
  type key
  type 'a dict
  val empty : 'a dict
  val insert : key -> 'a -> 'a dict -> 'a dict
  val remove : key -> 'a dict -> 'a dict
  val find_opt : key -> 'a dict -> 'a option
  val find : key -> 'a dict -> 'a
  val to_list : 'a dict -> (key * 'a) list
end

module MakeListDict (Ord: Map.OrderedType) : KDICT with type key = Ord.t = struct
  type key = Ord.t
  type 'a dict = (key * 'a) list

  let empty = []

  let rec insert key value dict =
    match dict with
    | [] -> [(key, value)]
    | (k, v) :: rest when Ord.compare k key = 0 -> (key, value) :: rest
    | pair :: rest -> pair :: insert key value rest
  
  let rec remove key dict =
    match dict with
    | [] -> []
    | (k, v) :: rest when Ord.compare k key = 0 -> rest
    | pair :: rest -> pair :: remove key rest

  let rec find_opt key dict =
    match dict with
    | [] -> None
    | (k, v) :: rest when Ord.compare k key = 0 -> Some v
    | _ :: rest -> find_opt key rest

  let rec find key dict =
    match dict with
    | [] -> failwith "Key not found"
    | (k, v) :: rest when Ord.compare k key = 0 -> v
    | _ :: rest -> find key rest

  let to_list dict = dict
end

module CharOrdered : Map.OrderedType with type t = char = struct
  type t = char
  let compare = Char.compare
end

module CharListDict = MakeListDict(CharOrdered)

module Freq (D : KDICT) = struct
  let freq (xs : D.key list) : (D.key * int) list =
    let rec count xs dict =
      match xs with
      | [] -> dict
      | h :: t ->
        let times = match D.find_opt h dict with
        | Some v -> v + 1
        | None -> 1
        in count t (D.insert h times dict)
    in let res = count xs D.empty
    in D.to_list res
end

let list_of_string s = String.to_seq s |> List.of_seq
module CharFreq = Freq(CharListDict)
let char_freq s =
  let chars = list_of_string s
  in CharFreq.freq chars