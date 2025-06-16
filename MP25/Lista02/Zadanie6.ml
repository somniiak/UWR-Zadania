let rec suffixes xs =
  match xs with
  | [] -> [[]]
  | h :: t -> xs :: suffixes t