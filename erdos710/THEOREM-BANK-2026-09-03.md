# Erdős #710 — harvested theorem bank

**Release status:** public mathematical archive.  
**Source:** MSL whole-day export, harvested 2026-09-03.  
**Claim discipline:** the labels below are the source-recorded statuses from the campaign. They are preserved rather than silently strengthened. The full asymptotic Erdős #710 target remains **OPEN**.

## T1 — Endpoint monotonicity — `PROVED`

Let `E(n)=n+f(n)`. Then `E(n)` is nondecreasing. Equivalently,

\[
f(n+1)\ge f(n)-1.
\]

Recorded proof idea: a valid assignment for `n+1` restricts to indices `<= n`.

## T2 — Primitive-antichain doubling reduction — `PROVED`

For a primitive antichain `A \subseteq [1,n]`, define

\[
M_A(x)=\#\{m\le x:\exists a\in A,\ a\mid m\}.
\]

The source-recorded Hall reduction states that the obstruction is equivalent to failure of

\[
M_A(n+h)\ge 2M_A(n),
\]

and therefore

\[
f(n)=\min\{h:M_A(n+h)\ge 2M_A(n)\text{ for every primitive }A\}.
\]

This became the campaign's standing arithmetic reformulation.

## T3 — Critical doubling identity — `PROVED`

At threshold, the source records existence of a critical primitive antichain satisfying

\[
M_A(n+f(n)-1)=2M_A(n)-1.
\]

## M1 — Exact finite threshold table — `COMPUTATION_SUPPORTED`

The campaign used the **inclusive** convention `t(n)` and recorded:

| n | t(n) |
|---:|---:|
| 50 | 76 |
| 100 | 160 |
| 150 | 246 |
| 200 | 340 |
| 300 | 510 |
| 500 | 877 |
| 1000 | 1816 |
| 2000 | 3814 |

### Convention warning

Elsewhere in the estate the open-interval `f` convention is one larger in examples such as `f(150)=247` and `f(200)=341`. These conventions are **not merged** here.

## M2 — Prime-descent finite law — `COMPUTATION_SUPPORTED`

The frozen check recorded

\[
t(p)=t(p-1)-1
\]

for every prime `p` in `[13,113]`, **25/25** tested primes.

An externally claimed extension to primes `<=1000` existed in the session, but this release preserves only the locally verified `p<=113` scope.

## M3 — Named-archetype refutation — `REFUTED`

The following candidate families failed to reproduce the true threshold for `n>=75` in the recorded finite campaign:

- tail intervals;
- Ω-level sets;
- prime-factor windows;
- mixed tails.

The Ω-level family was exact at `n=50` (`76=76`) and then fell short at larger recorded values, including `152<160`, `316<340`, and `474<510` by `n=300`.

This is a negative result, not a close of Erdős #710.

## M4 — Critical Hall-set structure — `COMPUTATION_SUPPORTED`

The extracted minimal Hall violator was recorded as a mixed-Ω hybrid rather than one of the simple named families.

Example at `n=150`:

- generator-set size: `13`;
- Ω distribution: `{1:2, 2:7, 3:4}`;
- tail fraction approximately `0.23`.

The standing successor target is to classify these critical antichains as an explicit generator family and certify exact reproduction on a frozen finite range.

---

# Sealed formalizer results recovered from the same export

The source export records three self-authored Lean theorems as `VERIFIED`, `FULL_FORMALIZATION`, externally statement-reviewed, and with clean axiom footprint. This file preserves the exact theorem statements where they were printed in the export.

## `feasible_iff_assignment`

```lean
theorem feasible_iff_assignment
    {α : Type*} [DecidableEq α]
    (n L : Nat) (S : Finset α) (k : α → Nat) :
    Feasible n L S k ↔
      ∃ f : α → Nat,
        Set.InjOn f (S : Set α) ∧
          ∀ x, x ∈ S → f x ∈ divNbhd n L (k x) := by
```

Interpretation recorded in-session: direct bridge between feasibility and the divisibility-matching formulation.

## `deficient_union_blocks_injection_repaired`

```lean
theorem deficient_union_blocks_injection_repaired
    {α β : Type*} [DecidableEq α] [DecidableEq β]
    (S : Finset α) (t : α → Finset β) (f : α → β)
    (hinj : Set.InjOn f (S : Set α))
    (hmem : ∀ x, x ∈ S → f x ∈ t x)
    (hdef : (S.biUnion t).card < S.card) :
    False := by
```

The `_repaired` suffix is part of the evidence trail: the first authored proof failed, kernel feedback was returned, and the repaired theorem then sealed.

## `bounded_feasible_threshold`

The export records the theorem meaning as: **a nonempty bounded feasible-length set has a least element**, supplying well-definedness for the finite threshold/minimum object. The exact source declaration was not printed in the harvested narrative, so this release does not invent Lean syntax for it.

## Provenance spine from the harvested session

The export records these relevant commits in the original research repository:

- `c02e635a05` — theorem harvest for Erdős #710;
- `f463dd3134` — first autonomous certified finite #710 lower-bound campaign;
- `e17e872133` — machine-authored theorem plus kernel repair loop;
- `dc7eef8b29` — three sealed self-authored #710 theorems.

## What this file does **not** claim

It does not claim Erdős #710 is solved. It does not upgrade `COMPUTATION_SUPPORTED` rows into universal theorems. It does not merge the inclusive `t(n)` convention with the open-interval `f(n)` convention. It does not claim historical novelty before literature adjudication.
