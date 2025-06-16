let build_list n f =
  let rec aux xs a =
    match a with
    | -1 -> xs
    | _ -> aux (f a :: xs) (a - 1)
  in aux [] (n - 1)

let negatives n = build_list n (fun v -> - v - 1)
let reciprocals n = build_list n (fun v -> 1.0 /. float_of_int (v + 1))
let evens n = build_list n (fun v -> v * 2)
let identityM n =
  build_list n (fun i ->
    build_list n (fun j -> if i = j then 1 else 0)
    )