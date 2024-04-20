import parser_gleam/parser as p
import parser_gleam/char as c
import parser_gleam/string as s

type Regex {
  Empty
  Epsilon
  Literal(String)
  Union(Regex, Regex)
  Concat(Regex, Regex)
  Kleene(Regex)
}

fn regex() {
  
}