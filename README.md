# Erdős 710 prime descents and an Erdős 1044 closed form

An **observed prime-descent law for Erdős 710 tested with five held-out primes**, five Lean Hall-matching theorems supporting the computation, and a **closed form for the Erdős 1044 extremal family**.

Author: Jared Wilder. First public timestamp: 2026-09-10.

## Erdős 710 — prime-descent law

Let `f(n)` be the minimal `L` such that the open interval `(n,n+L)` contains distinct integers `a_1,...,a_n` with `k | a_k` for every `k`.

The function was computed exhaustively through `n <= 114`. The following three patterns hold throughout that range:

```text
LAW-1  f(p) < f(p-1) for every prime 13 <= p <= 113.   25/25, no exceptions.
LAW-2  f(p) <= f(p-1) for every prime p >= 5 in range.  5, 7, 11 give equality.
LAW-3  every descent of f in [1,114] has magnitude exactly 1.
```

The five largest tested primes—**101, 103, 107, 109, 113**—were withheld while the pattern was formulated and computed afterward. All five agreed with the pre-stated law.

### Finite range and computation

- `p=2` and `p=3` are ascents, so LAW-1 starts at 13 and LAW-2 at 5.
- Primality is sufficient for descent in the tested range but not necessary; composite descents also occur.
- Historical novelty has not been adjudicated beyond the problem page.

The values come from exhaustive Hall bipartite matching, incrementing from `L=n+1`, with Hall deficit zero at every accepted point. `e710.py`, `hall.py`, `fast.py`, `ratios.json`, and `ratios-big.json` contain the computation.

The source notes the relevant asymptotic literature of Erdős–Pomerance (1980).

## Five Lean Hall theorems

`sealed-library/` contains five kernel-verified Lean theorems with clean axiom footprints:

- `hall_deficiency_blocks` — a deficient witness set admits no injective transversal;
- `deficient_union_blocks_injection_repaired` — a repaired union-deficiency lemma;
- `feasible_iff_assignment`;
- `bounded_feasible_threshold`;
- `e710_lower_bound_50`.

A historical metadata error is preserved because it is instructive: `e710_lower_bound_50` was once mislabelled as `R(5,5) >= 50`. The theorem itself is an Erdős 710 Hall-deficiency lower-bound result; only the label was wrong.

`erdos710-formalizer/` retains the historical formalization records and receipts that produced this library.

## Erdős 1044 — closed form for the extremal family

Tang proved in 2026 that the infimum of `Lambda` over all degrees is 2. This repository contributes the exact family formula

```text
Lambda(z^n - 1)
= (2 sqrt(pi) / n) * 2^(1/n - 1) * Gamma(1/2n) / Gamma(1/2n + 1/2)
```

with monotone decrease and asymptotic

```text
2 + 4 ln 2 / n + O(1/n^2).
```

The formula is numerically checked to satisfy `Lambda > 2` for every degree `2 <= n <= 25`.

## Mathematical status

For Erdős 710, the prime-descent statement is a finite empirical law through `n<=114`, strengthened by a genuine five-prime held-out test and supported by a separate Lean Hall-theorem library.

For Erdős 1044, the contribution is the exact closed form and its asymptotic/finite numerical checks; Tang's theorem supplies the global infimum result.

## License

Apache-2.0.