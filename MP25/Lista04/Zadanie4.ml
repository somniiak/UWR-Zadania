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

(* https://ocaml.org/manual/5.2/api/Map.Make.html#maps *)

module MakeMapDict (Ord: Map.OrderedType) : KDICT with type key = Ord.t = struct
  module Tmap = Map.Make(Ord)
  type key = Ord.t
  type 'a dict = 'a Tmap.t

  let empty = Tmap.empty
  let insert key value dict = Tmap.add key value dict
  let remove key dict = Tmap.remove key dict
  let find_opt key dict = Tmap.find_opt key dict
  let find key dict = Tmap.find key dict
  let to_list dict = Tmap.bindings dict
end

module CharOrdered : Map.OrderedType with type t = char = struct
  type t = char
  let compare = Char.compare
end

module CharMapDict = MakeMapDict(CharOrdered)