# erdos710-descent-and-1044

An **observed prime-descent law for Erdős 710 with five held-out primes**, five sealed Hall-matching
theorems behind the computation, and a **closed form for the Erdős 1044 extremal family**.

Author: Jared Wilder. First public timestamp: 2026-09-10.

## Erdős 710 — prime-descent law

Let `f(n)` be the minimal `L` such that the open interval `(n,n+L)` contains distinct integers
`a_1,...,a_n` with `k | a_k` for every `k`.

**Evidence class: exhaustive finite observation through `n <= 114`, with five primes held out and
computed only after the law was stated.**

    LAW-1 (strong)  f(p) < f(p-1) for every prime 13 <= p <= 113.  25/25, no exceptions.
    LAW-2 (weak)    f(p) <= f(p-1) for every prime p >= 5 in range.     5, 7, 11 give equality.
    LAW-3 (step)    every descent of f in [1,114] has magnitude exactly 1.

The held-out primes were **101, 103, 107, 109, 113**. Their agreement with the pre-stated law is
the strongest part of the finite evidence because they were tests, not fit points.

### Exact finite boundary

- `p=2` and `p=3` are ascents, so LAW-1 starts at 13 and LAW-2 at 5.
- Primality is sufficient in the tested range but not necessary; composite descents also occur.
- Historical novelty has not been adjudicated beyond the problem page.

The values come from exhaustive Hall bipartite matching, unseeded and incremental from `L=n+1`,
with Hall deficit zero at every computed point. `e710.py`, `hall.py`, `fast.py`, `ratios.json`, and
`ratios-big.json` carry the computation.

Known asymptotic literature, recorded in the source, is Erdős–Pomerance 1980.

## Five sealed Hall theorems

`sealed-library/` holds five Lean theorems, each kernel-verified with a clean axiom footprint:

- `hall_deficiency_blocks` — a deficient witness set admits no injective transversal;
- `deficient_union_blocks_injection_repaired` — authored, failed at the kernel, re-authored and
  sealed;
- `feasible_iff_assignment`;
- `bounded_feasible_threshold`;
- `e710_lower_bound_50`.

A label correction is preserved because it is semantically important: an automated reader once
described `e710_lower_bound_50` as `R(5,5) >= 50`. It is not a Ramsey statement; it is an Erdős 710
Hall-deficiency lower-bound theorem. The correction changes the label, not the theorem.

`erdos710-formalizer/` carries the campaign directories and receipts that produced the sealed
library.

## Erdős 1044 — closed form for the extremal family

Tang proved in 2026 that the infimum of `Lambda` over all degrees is 2. This repository contributes
the exact family formula

`Lambda(z^n - 1) = (2 sqrt(pi) / n) * 2^(1/n - 1) * Gamma(1/2n) / Gamma(1/2n + 1/2)`

with monotone decrease and asymptotic

`2 + 4 ln 2 / n + O(1/n^2)`.

The formula is numerically checked to satisfy `Lambda > 2` for every degree `2 <= n <= 25`.

### Scope

For Erdős 710, the prime-descent law is a finite observed law with a genuine held-out test and a
separate sealed theorem library underneath it. For Erdős 1044, the contribution is the exact closed
form and its finite numerical checks; Tang's theorem supplies the global infimum result.

## License

Apache-2.0.
