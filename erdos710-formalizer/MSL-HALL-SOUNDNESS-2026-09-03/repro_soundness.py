"""Prove the REAL general theorem: a deficient witness set blocks any injective
transversal. This is the soundness core of the whole Hall-deficiency argument — a
genuine mathematical theorem about matchings, proved by counting (image subset +
injective card + card_le contradiction), clean axioms, NO per-n arithmetic."""
import os, sys
root = os.environ["CLAUDE_PROJECT_DIR"]
sys.path.insert(0, root)
from oracle.tools.msl_lean_cable import run_obligation

defs = r"""
/-- A witness set `S` is *deficient* for neighborhood map `t` when the union of
    neighborhoods of `S` is strictly smaller than `S` itself. -/
def Deficient {ι α : Type*} [DecidableEq α] (t : ι → Finset α) (S : Finset ι) : Prop :=
  (S.biUnion t).card < S.card
"""

concl = (r"""forall {iota : Type*} {alpha : Type*}, forall [inst : DecidableEq alpha],
  forall (t : iota -> Finset alpha) (S : Finset iota),
    Deficient t S ->
    ~ (exists f : iota -> alpha, Set.InjOn f (S : Set iota) /\ (forall i, i in S -> f i in t i))""")

proof = r"""by
  intro iota alpha inst t S hdef
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
"""

# ascii -> lean unicode the cable/Lean expects
concl = (concl.replace("forall", "∀").replace("~", "¬").replace("exists", "∃")
         .replace("/\\", "∧").replace("->", "→").replace(" in ", " ∈ "))

r = run_obligation({"id": "hall-deficiency-blocks", "imports": "Mathlib",
                    "definitions": defs, "conclusion": concl, "proof": proof},
                   timeout=180)
print("FORMAL_STATUS:", r.get("formal_status"))
print("AXIOMS:", r.get("axioms"))
print("EVENTS:", (r.get("events") or [])[:5])
