# TARGET: the prime-descent law of Erdős #710's f(n) — 2026-09-02

Status: OBSERVED (TESTED_FAMILY, n <= 114). Not a theorem. Not in the literature that we
have checked (which is: the erdosproblems.com #710 page only — prior-art check NOT run).
Openness of #710 itself is the source's marking, not ours.

## The function

f(n) = minimal L such that the open interval (n, n+L) contains distinct integers
a_1, ..., a_n with k | a_k for all 1 <= k <= n.

Convention (matches e710.py in this directory): candidates are the integers in
[n+1, n+L-1]. Computed by exhaustive Hall/bipartite matching, unseeded, incremental
from L = n+1. Hall deficit was 0 at every computed (n, f(n)).

## The observed laws

```text
LAW-1 (strong)   f(p) < f(p-1) for EVERY prime p with 13 <= p <= 113.   25/25, no exceptions.
LAW-2 (weak)     f(p) <= f(p-1) for every prime p >= 5 in range.        (5, 7, 11 give equality)
LAW-3 (step)     every descent of f in [1,114] has magnitude exactly 1: f(n) = f(n-1) - 1.
```

Boundary facts, stated so nobody overclaims:

- p = 2, 3 are ASCENTS (f(1)=2, f(2)=3, f(3)=4). LAW-1 starts at 13; LAW-2 at 5.
- Primality is sufficient-in-range, NOT necessary: composite descents exist
  (33, 34, 49, 51, 57, 58, 62, 65, 66, 74, 76, 77, 82, 85, 86, 87, 91-95, 99, ...).
- The 25 confirming primes: 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
  101 103 107 109 113. The last five were computed 2026-09-02 PM, AFTER the law was
  conjectured from the first twenty — a genuine out-of-sample pass.

## FALSIFIER

MEASURE f(p) and f(p-1) for the next primes: 127, 131, 137, 139, 149, ...
THE CLAIM (LAW-1) IS DEAD IF any prime p >= 13 has f(p) >= f(p-1).

```bash
python oracle/evidence/erdos710/e710.py 150
```

(~minutes; the matcher is exact and unseeded. Read f(p) and f(p-1) off the table; the
DESCENTS line at the bottom is the machine's own receipt.)

## Why it might be provable (hint-grade, CLAIM_STATUS NONE)

Stepping n-1 -> n changes exactly two things: the constraint set gains the single index
n (cheapest witness 2n, always inside the window since f(n) > n), and the window's left
edge slides up by one. A descent at n says the Hall bottleneck governing f(n-1) was NOT
tightened by either change — i.e. at a prime p, the binding tight set for f(p-1) does not
contain the new index and gains slack from the shifted edge. Identify the tight
(Hall-critical) index set at each n — forced_deficit() in e710.py is a start — and
characterize when the new index p joins it. Primality should enter because p shares no
divisor structure with any smaller index, so p's candidate multiples collide least with
the congested small-k residue classes. LAW-3 (unit steps) suggests the bottleneck moves
by single-integer edge effects, which is what makes a local proof plausible.

A proof of LAW-1 would be a small unconditional result attached to an open Erdős problem
(#710, prize-bearing). It does NOT by itself resolve #710's asymptotic question — claim
ceiling stated so the two are never conflated.

## Provenance

- Enumeration: oracle/evidence/erdos710/e710.py (Hall matching, exhaustive, deficit
  receipts inline), runs to n=114 on 2026-09-02.
- Found during the Haiku MSL v1.7 inaugural A/B run (decode by Fable 5, same day).
  Haiku reported the diluted form "47.6% of descents are primes"; the 100%-of-primes
  form and the out-of-sample extension to 113 were added at decode time.
- Companion lesson file: oracle/frontier_formalizer/MSL-1.7/UPGRADE-CANDIDATES-HAIKU-AB-2026-09-02.md
