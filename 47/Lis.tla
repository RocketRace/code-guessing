------------------------- MODULE Lis ---------------
EXTENDS Sequences, Naturals

CONSTANTS Sequence
ASSUME Sequence \in Seq(Nat)

IsIncreasingSubsequence(indices) ==
    /\  Len(indices) <= Len(Sequence)
    /\  \A i \in 1 .. Len(indices) :
            indices[i] <= Len(Sequence)
    /\  \/  Len(indices) <= 1
        \/  /\  Len(indices) > 1
            /\  \A i \in 1 .. Len(indices) - 1 :
                indices[i] < indices[i + 1]
            /\  \A i \in 1 .. Len(indices) - 1 :
                Sequence[indices[i]] < Sequence[indices[i + 1]]

IsSolution(candidate) ==
    LET length == Len(candidate)
        subsequences == UNION {[1 .. n -> 1..Len(Sequence)] : n \in 0..Len(Sequence) }
    IN  /\ IsIncreasingSubsequence(candidate)
        /\ \A subsequence \in subsequences:
            \/  ~ IsIncreasingSubsequence(subsequence)
            \/  /\  IsIncreasingSubsequence(subsequence)
                /\  Len(subsequence) <= length

VARIABLES candidates, solutions

Init ==
    /\  candidates = { <<n>> : n \in 1..Len(Sequence) }
    /\  solutions =  {}

Extend == \E candidate \in candidates :
    LET start == candidate[Len(candidate)]
        highest == Sequence[start]
        options == { n \in (start + 1)..Len(Sequence) : Sequence[n] > highest }
        extensions == { Append(candidate, option) : option \in options }
    IN  IF extensions = {}
        THEN
            LET updated == solutions \cup {candidate}
                lengths == { Len(solution) : solution \in updated }
                filtered == { solution \in updated : (\A length \in lengths: Len(solution) >= length)}
            IN  /\  candidates' = candidates \ {candidate}
                /\  solutions' = filtered
        ELSE
            /\  candidates' = (candidates \ {candidate}) \cup extensions
            /\  UNCHANGED solutions
                
Spec == Init /\ [][Extend]_<<candidates, solutions>>
Invariant == candidates = {} => \A solution \in solutions: 
    IsSolution(solution) 
  
Termination == <>(candidates = {})

NoSolutions == solutions = {}

=============================================================================

