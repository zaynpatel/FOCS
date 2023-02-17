(*(let rec squares xs = 
  match xs with 
  (* list is either empty or not empty *)
  | [] -> []
  | x::xs' -> (x * x) :: (squares xs') (* x ... squares xs' -> these are the options available *)

(*
   [2;3;4;5]
   x = 2
   xs' = [3;4;5]
   squares xs' -> [9;16;25]
  [4;9;16;25]
*)
(* with higher order function *)



let rec squares xs = 
  match xs with 
  | [] -> []
  | x::xs' -> (square x) :: (squares xs')



let rec doubles xs = 
  match xs with 
  | [] -> []
  | x::xs' -> (double x) :: (doubles xs')) *)

let double x = 2 * x;;
let square x = x * x;;

let rec map f xs = 
  match xs with 
  | [] -> []
  | x::xs' -> (f x) :: (map f xs')

let doubles xs = 
  map double xs

let squares xs = 
  map square xs 


let positive x = (x >= 0)


let rec positives xs = 
  match xs with
  | [] -> []
  | x::xs' -> if positive x then x :: (positives xs') else (positives xs')

let scale a xs = 
  map (fun x -> a * x) xs

let scaler x = (a * x) (* unbound value error because a doesn't know wht this value is *)

let makeScaler a = (fun x -> (a * x))

let scale a xs = 
  map (makeScaler a) xs
