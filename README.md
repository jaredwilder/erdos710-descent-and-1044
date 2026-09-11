# erdos710-descent-and-1044

An observed prime-descent law for Erdos #710 with five primes held out as a live test, the sealed
Hall-matching theorems behind the machine work on that problem, and a closed form for the Erdos
#1044 extremal family.

Author: Jared Wilder. First public timestamp: 2026-09-10.

## Erdos 710: the prime-descent law

f(n) is the minimal L such that the open interval (n, n+L) contains distinct integers
a_1, ..., a_n with k dividing a_k for every k.

**Status, in the source document's own third line: OBSERVED, tested family n <= 114. NOT A
THEOREM.**

    LAW-1 (strong)  f(p) < f(p-1) for EVERY prime p with 13 <= p <= 113.  25/25, no exceptions.
    LAW-2 (weak)    f(p) <= f(p-1) for every prime p >= 5 in range.       5, 7, 11 give equality.
    LAW-3 (step)    every descent of f in [1,114] has magnitude exactly 1.

**The five primes 101, 103, 107, 109, 113 were computed after the law was stated.** That makes
them a held-out test rather than a fit, which is the reason this document is worth reading at all.

Boundary facts the document states so that nobody overclaims:

- p = 2 and p = 3 are **ascents**. LAW-1 starts at 13, LAW-2 at 5.
- Primality is sufficient in range but **not necessary**: composite descents exist at 33, 34, 49,
  51, 57, 58, 62, 65, 66, 74, 76, 77, 82, 85, 86, 87, 91 through 95, 99, and more.
- Prior art was **not** checked beyond the problem's own page, and the document says so.

Values come from exhaustive Hall bipartite matching, unseeded, incremental from L = n+1, with Hall
deficit 0 at every computed point. `e710.py`, `hall.py` and `fast.py` are here; `ratios.json` and
`ratios-big.json` carry the computed values.

Known literature for the asymptotics, recorded in the source: Erdos-Pomerance 1980 brackets f(n)
between (2 / sqrt e) n sqrt(log n / log log n) and 1.7398 n sqrt(log n).

## The sealed theorems

`sealed-library/` holds five Lean theorems, each kernel-verified with a clean axiom footprint:

- `hall_deficiency_blocks` — a deficient witness set admits no injective transversal. The Hall
  soundness core.
- `deficient_union_blocks_injection_repaired` — authored, failed at the kernel, re-authored,
  sealed.
- `feasible_iff_assignment`, `bounded_feasible_threshold`, `e710_lower_bound_50`.

**A label correction, recorded here because it nearly propagated:** an automated reader described
`e710_lower_bound_50` as "R(5,5) >= 50". It is **not** a Ramsey result. It states that a specific
deficient index set admits no injective transversal into its divisibility neighborhood, which is
an Erdos 710 lower bound. R(5,5) >= 50 would contradict the literature and is not claimed anywhere
in this work.

`erdos710-formalizer/` carries the campaign directories that produced them, with receipts.

## Erdos 1044

`erdos1044/` — Tang proved in 2026 that the infimum of Lambda over all degrees is 2. This work
contributes a **closed form for the extremal family**:

    Lambda(z^n - 1) = (2 sqrt(pi) / n) * 2^(1/n - 1) * Gamma(1/2n) / Gamma(1/2n + 1/2)

verified monotone decreasing with asymptotic 2 + 4 ln 2 / n + O(1/n^2), and checked to satisfy
Lambda > 2 at every degree from 2 to 25.

**This is a closed form plus bounded numerical verification. It is not a proof of #1044.**

## License

Apache-2.0.
