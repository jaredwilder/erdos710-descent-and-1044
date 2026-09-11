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

theorem feasible_iff_assignment
    {α : Type*} [DecidableEq α]
    (n L : Nat) (S : Finset α) (k : α → Nat) :
    Feasible n L S k ↔
      ∃ f : α → Nat,
        Set.InjOn f (S : Set α) ∧
          ∀ x, x ∈ S → f x ∈ divNbhd n L (k x) := by
  constructor
  · intro h
    exact h
  · intro h
    exact h

#print axioms feasible_iff_assignment
