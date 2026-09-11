import Mathlib
set_option autoImplicit false

def feasibleLengthsUpTo
    (P : Nat → Prop) [DecidablePred P] (U : Nat) : Finset Nat :=
  (Finset.range (U + 1)).filter P

theorem bounded_feasible_threshold
    (P : Nat → Prop) [DecidablePred P]
    (L U : Nat)
    (hP : P L)
    (hLU : L ≤ U) :
    ∃ m ∈ feasibleLengthsUpTo P U, ∀ q ∈ feasibleLengthsUpTo P U, m ≤ q := by
  have hnonempty : (feasibleLengthsUpTo P U).Nonempty := by
    refine ⟨L, ?_⟩
    unfold feasibleLengthsUpTo
    exact Finset.mem_filter.mpr
      ⟨Finset.mem_range.mpr (Nat.lt_succ_of_le hLU), hP⟩
  refine ⟨(feasibleLengthsUpTo P U).min' hnonempty, ?_, ?_⟩
  · exact (feasibleLengthsUpTo P U).min'_mem hnonempty
  · intro q hq
    exact (feasibleLengthsUpTo P U).min'_le q hq

#print axioms bounded_feasible_threshold
