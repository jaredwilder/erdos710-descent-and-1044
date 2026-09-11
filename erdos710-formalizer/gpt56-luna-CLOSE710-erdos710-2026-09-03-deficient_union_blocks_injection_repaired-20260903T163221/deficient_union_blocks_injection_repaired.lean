import Mathlib
set_option autoImplicit false

theorem deficient_union_blocks_injection_repaired
    {α β : Type*} [DecidableEq α] [DecidableEq β]
    (S : Finset α) (t : α → Finset β) (f : α → β)
    (hinj : Set.InjOn f (S : Set α))
    (hmem : ∀ x, x ∈ S → f x ∈ t x)
    (hdef : (S.biUnion t).card < S.card) :
    False := by
  have himage : S.image f ⊆ S.biUnion t := by
    intro y hy
    rcases Finset.mem_image.mp hy with ⟨x, hx, rfl⟩
    exact Finset.mem_biUnion.mpr ⟨x, hx, hmem x hx⟩
  have hcard : (S.image f).card = S.card :=
    Finset.card_image_of_injOn hinj
  have hle : S.card ≤ (S.biUnion t).card := by
    calc
      S.card = (S.image f).card := hcard.symm
      _ ≤ (S.biUnion t).card := Finset.card_le_card himage
  exact (Nat.not_le_of_lt hdef) hle

#print axioms deficient_union_blocks_injection_repaired
