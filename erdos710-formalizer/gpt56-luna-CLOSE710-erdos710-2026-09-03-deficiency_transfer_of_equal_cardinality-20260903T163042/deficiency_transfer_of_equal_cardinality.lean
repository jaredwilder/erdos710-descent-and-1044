import Mathlib
set_option autoImplicit false

theorem deficiency_transfer_of_equal_cardinality
    {α β : Type*} [DecidableEq α] [DecidableEq β]
    (P S : Finset α) (t : α → Finset β)
    (hPS : P ⊆ S)
    (hcard : P.card = S.card)
    (hdef : (P.biUnion t).card < P.card) :
    (S.biUnion t).card < S.card := by
  have hunion : P.biUnion t ⊆ S.biUnion t := by
    intro y hy
    rw [Finset.mem_biUnion] at hy ⊢
    obtain ⟨x, hx, hyx⟩ := hy
    exact ⟨x, hPS hx, hyx⟩
  have hle : (P.biUnion t).card ≤ (S.biUnion t).card :=
    Finset.card_le_card hunion
  have hlt : (S.biUnion t).card < P.card := by
    exact lt_of_le_of_lt hle hdef
  simpa [hcard] using hlt

#print axioms deficiency_transfer_of_equal_cardinality
