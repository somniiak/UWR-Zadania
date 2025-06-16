let empty_set _ = false;;
let singleton a x = x = a;;
let in_set a s = s a;;
let union s t x = (s x) || (t x);;
let intersection s t x = (s x) && (t x);;