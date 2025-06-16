let rec insert x l =
  match l with
  | [] -> [x]
  | h :: t -> if x <= h then x :: l else h :: insert x t

let rec insertion_sort l =
  match l with
  | [] -> []
  | h :: t -> insert h (insertion_sort t)

let y = insertion_sort [5; 4; 3; 2; 1]

(*

Pomocniczy lemat (o funkcji insert)

Twierdzenie pomocnicze:
  Jeśli l jest posortowaną niemalejąco listą, to insert x l jest
  również posortowaną niemalejąco listą.

Dowód przez indukcję po strukturze listy l

Podstawa induckji (l = []):
  - insert x [] = [x] — posortowana lista jednoelementowa

Krok indukcyjny:
  - Założenie indukcyjne (l = h :: t):
  
  - Dowód:
    * Zakładamy że h <= t[0], t[0] <= t[1], ... i insert x t jest posortowana.
    * Jeśli x <= h, to insert x (h :: t) = x :: h :: t — i x <= h, a h :: t jest już posortowane.
    * Jeśli x > h, to insert x (h :: t) = h :: insert x t.
      Z założenia indukcyjnego: insert x t jest posortowana,
      a h <= insert x t[0], bo h <= t[0] i x > h, więc również porządek się zachowuje.

    Zachodzi.

*)

(*

Dowód przez indukcję względem długości listy l

Podstawa indukcji (|l| = 0):
  - insertion_sort [] = []
  - Lista pusta jest trywialnie posortowana.

Krok indukcyjny:
  - Założenie indukcyjne:
    Zakładamy, że dla listy t o długości n, insertion_sort t
    jest posortowana niemalejąco.

  - Cel:
    Pokażemy, że insertion_sort (h :: t) jest także posortowana.

  - Dowód:
    * insertion_sort (h :: t) = insert h (insertion_sort t)
    * Z założenia indukcyjnego: insertion_sort t jest posortowana niemalejąco.

    * Pozostaje pokazać, że insert h sorted_t (gdzie sorted_t = insertion_sort t)
      zachowuje porządek niemalejący.

    
    * insertion_sort t — posortowana (z założenia)
    * insert h (insertion_sort t) — posortowana (z lematu)

    Zachodzi.

*)