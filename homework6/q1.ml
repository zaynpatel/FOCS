(* Question 1: Context-free grammar creation *) 

let q1a : grammar = {
  nonterms = ["S"; "B"; "C"];
  terms = ["a"; "b"; "c"];
  rules = [ ("S", "aSb");
            ("S", "aB");
            ("B", "bBc");
            ("B", "C");
            ("C", "cC");
            ("C", "") ];
  start = "S"
}


let q1b : grammar = {
  nonterms = ["S"; "A"];
  terms = ["a"; "b"; "c"];
  rules = [ ("S", "aSc");
            ("S", "aAc");
            ("A", "bAc");
            ("A", "")
            ];
  start = "S"
}

let q1c : grammar = {
  nonterms = ["S"; "A"; "B"];
  terms = ["a"; "b"; "c"];
  rules = [ ("S", "AB");
            ("A", "aaAbB");
            ("B", "bBc");
            ("B", "")
            ];
  start = "S"
}

                
let q1d : grammar = {
  nonterms = ["S"];
  terms = ["a"; "b"];
  rules = [ ("S", "aSb");
            ("S", "bSa");
            ("S", "SS") 
            ];
  start = "S"
}

             
let q1e : grammar = {
  nonterms = ["S"; "A"];
  terms = ["1"; "+"; "="];
  rules = [ ("S", "1S1");
            ("S", "+A");
            ("A", "1A1");
            ("A", "=")
            ];
  start = "S"
}
