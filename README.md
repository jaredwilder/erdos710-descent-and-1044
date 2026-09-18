# Erdős #710 finite Hall data and an Erdős #1044 closed form

Two independent results are collected here: an exact finite study of the Hall-matching function in Erdős #710, and a closed formula for the extremal family `z^n-1` in Erdős #1044.

## Erdős #710 — exact values through `n=114`

Let `f(n)` be the least `L` such that the open interval `(n,n+L)` contains distinct integers

\[
a_1,\ldots,a_n
\]

with

\[
k\mid a_k\qquad(1\le k\le n).
\]

The repository computes `f(n)` exhaustively through

\[
\boxed{n\le114}
\]

using exact bipartite matching.

Three finite patterns hold throughout that computed range:

```text
for every prime 13 <= p <= 113:   f(p) < f(p-1)
for every prime  5 <= p <= 113:   f(p) <= f(p-1)
every descent of f on [1,114] has size exactly 1
```

There are 25 primes in the first range, with no exceptions. At `p=5,7,11` the second inequality is an equality. Composite descents also occur, so primality is not a necessary condition for a drop.

These are **exact finite observations through 114**, not an unbounded prime-descent theorem.

The final five primes in the computation—`101,103,107,109,113`—were evaluated after the pattern had been formulated, and all five agree with it. This provides an out-of-sample finite check but does not change the theorem status of the unbounded statement.

## Hall-matching formulation

The finite computation is an exact Hall/matching problem. For each candidate interval length `L`, the program asks whether the divisibility constraints admit an injective assignment of representatives.

The source programs are:

- `e710.py`;
- `hall.py`;
- `fast.py`;
- `ratios.json` and `ratios-big.json`.

The computation increments `L` until a feasible matching is found; accepted values have zero Hall deficit.

## Lean Hall lemmas

`sealed-library/` contains five verified Lean theorems supporting the matching formulation:

- `hall_deficiency_blocks` — a deficient witness set rules out an injective transversal;
- `deficient_union_blocks_injection_repaired` — union-deficiency lemma;
- `feasible_iff_assignment` — equivalence between the finite matching model and assignment formulation;
- `bounded_feasible_threshold` — finite threshold statement;
- `e710_lower_bound_50` — a concrete Erdős #710 lower-bound certificate.

The historical records once attached an unrelated Ramsey label to `e710_lower_bound_50`; the theorem itself is an Erdős #710 Hall-deficiency statement. `erdos710-formalizer/` retains the original formalization receipts.

## Erdős #1044 — exact formula for `z^n-1`

For the extremal family `z^n-1`, the repository derives

\[
\boxed{
\Lambda(z^n-1)
=\frac{2\sqrt\pi}{n}\,2^{1/n-1}
\frac{\Gamma(1/2n)}{\Gamma(1/2n+1/2)}
}.
\]

The formula is monotone decreasing in `n` and has asymptotic expansion

\[
\boxed{
\Lambda(z^n-1)
=2+\frac{4\log2}{n}+O(n^{-2}).
}
\]

Direct numerical checks give `Lambda>2` for every degree `2<=n<=25`.

Tang's 2026 theorem supplies the global result that the infimum over all degrees is 2. The contribution here is the exact family formula and its asymptotic analysis.

## Scope

For Erdős #710, the repository provides exact finite data, a matching formulation, and Lean lemmas; the observed prime-descent pattern is not claimed beyond the computed range.

For Erdős #1044, the displayed formula for the family `z^n-1` is the mathematical result, with the global infimum attributed to Tang.

Author: Jared Wilder. License: Apache-2.0.
