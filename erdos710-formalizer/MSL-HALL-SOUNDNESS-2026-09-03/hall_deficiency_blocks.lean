import Mathlib
set_option autoImplicit false

/-- A witness set `S` is *deficient* for neighborhood map `t` when the union of the
    neighborhoods of `S` is strictly smaller than `S` itself. -/
def Deficient {iota alpha : Type*} [DecidableEq alpha] (t : iota → Finset alpha)
    (S : Finset iota) : Prop := (S.biUnion t).card < S.card

/-- Soundness of the Hall-deficiency certificate: a deficient witness set admits no
    injective transversal (no system of distinct representatives choosing, for each
    element of `S`, a member of its neighborhood). -/
theorem hall_deficiency_blocks {iota alpha : Type*} [DecidableEq alpha]
    (t : iota → Finset alpha) (S : Finset iota) (hdef : Deficient t S) :
    ¬ (∃ f : iota → alpha, Set.InjOn f (S : Set iota)
        ∧ (∀ i, i ∈ S → f i ∈ t i)) := by
  rintro ⟨f, hinj, hmem⟩
  have hsub : S.image f ⊆ S.biUnion t := by
    intro y hy
    simp only [Finset.mem_image] at hy
    obtain ⟨i, hi, rfl⟩ := hy
    exact Finset.mem_biUnion.mpr ⟨i, hi, hmem i hi⟩
  have hcard : (S.image f).card = S.card := Finset.card_image_of_injOn hinj
  have hle := Finset.card_le_card hsub
  rw [hcard] at hle
  exact absurd hle (Nat.not_le.mpr hdef)

#print axioms hall_deficiency_blocks
