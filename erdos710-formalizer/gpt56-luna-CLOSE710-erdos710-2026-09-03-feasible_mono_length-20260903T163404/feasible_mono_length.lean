import Mathlib
set_option autoImplicit false

def divNbhd (n L k : Nat) : Finset Nat :=
  (Finset.Ioo n (n + L)).filter (fun v => k ∣ v)

def Feasible
    {α : Type*} [DecidableEq α]
    (n L : Nat) (S : Finset α) (k : α → Nat) : Prop :=
  ∃ f : α → Nat,
    Set.InjOn f (S : Set α) ∧
      ∀ x, x ∈ S → f x ∈ divNbhd n L (k x)

theorem divNbhd_mono_length
    (n L M k : Nat)
    (hLM : L ≤ M) :
    divNbhd n L k ⊆ divNbhd n M k := by
  intro v hv
  have hv' := Finset.mem_filter.mp hv
  apply Finset.mem_filter.mpr
  constructor
  · exact Finset.mem_Ioo.mpr
      ⟨hv'.1.1, le_trans hv'.1.2 (Nat.add_le_add_left hLM n)⟩
  · exact hv'.2

theorem feasible_mono_length
    {α : Type*} [DecidableEq α]
    (n L M : Nat) (S : Finset α) (k : α → Nat)
    (hLM : L ≤ M)
    (hfeas : Feasible n L S k) :
    Feasible n M S k := by
  rcases hfeas with ⟨f, hinj, hmem⟩
  refine ⟨f, hinj, ?_⟩
  intro x hx
  exact divNbhd_mono_length n L M (k x) hLM (hmem x hx)

#print axioms feasible_mono_length
