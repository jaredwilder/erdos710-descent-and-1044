# RESOLUTION-INPUT — answer to REQUEST TARGET_KEY T710_ASYMPTOTIC_SOURCE

Filed by the harness servicing your REQUEST KIND SOURCE / NEW_INPUT. This file's
name matches your declared watchdog pattern; the content is the full source note
(also at ERPO80-SOURCE-NOTE.md). Statuses are load-bearing: RECEIPTED vs
KNOWLEDGE-DERIVED vs MISS. No theorem-level proof text is included — the honest
ceiling for claims about the paper's method remains CITED.

---

# SOURCE NOTE — the [ErPo80] and [Er92c] references for Erdős #710 (2026-09-03)

Filed to service a live REQUEST KIND SOURCE (TARGET_KEY T710_ASYMPTOTIC_SOURCE) from the
running CLOSE campaign. Every row carries its verification status. A status below
RECEIPTED means: usable as a lead, never as machine truth.

## RECEIPTED (from the frozen page capture, oracle/evidence/formalizer-sources/erdos/raw-erdos-710.html, sha in entry-graph)

- The problem is "A problem of Erdős and Pomerance [ErPo80], who proved
  (2/sqrt(e)+o(1)) n (log n/log log n)^(1/2) <= f(n) <= (1.7398...+o(1)) n (log n)^(1/2)."
- "In [Er92c] Erdős offered 2000 rupees for an asymptotic formula."
- The page's bibliography is loaded dynamically (fetch /bibs/<key>) and is NOT in the
  frozen capture; erdosproblems.com returns 403 to this harness's fetcher.

## KNOWLEDGE-DERIVED, UNVERIFIED THIS SESSION (a lead, not a receipt)

- [ErPo80] is, with high confidence: P. Erdős and C. Pomerance, "Matching the natural
  numbers up to n with distinct multiples in another interval", Nederl. Akad. Wetensch.
  Proc. Ser. A 83 (= Indag. Math. 42) (1980), 147-161. This is the canonical
  Erdős-Pomerance 1980 paper on exactly this matching problem.
- The Erdős papers archive at users.renyi.hu/~p_erdos/ carries scanned PDFs named by
  year; the 1980 Pomerance matching paper should be among the 1980-*.pdf files. The
  archive index page truncates in our fetch window before 1980, so the exact filename is
  unconfirmed here.
- [Er92c] is one of Erdős's early-1990s problem-collection papers (the rupee prizes are
  characteristic of them); exact identification unconfirmed here.

## ACQUISITION MISS (recorded so nobody mistakes it for coverage)

The federated literature door (noveltyforge acquire, receipted in erpo80-acquire.log +
erpo80-corpus.json) returned 30 papers, 0 Erdős-linked, 0 Pomerance-linked — generic
number-theory textbooks. The corpus does NOT contain the source and must not be cited as
if it did.

## WHAT THE CAMPAIGN CAN DO WITH THIS

The load-bearing content of [ErPo80] for the current bottleneck is its METHOD: how the
lower bound (2/sqrt(e)) n (log n/log log n)^(1/2) is forced — which family of indices
creates the obstruction — and how the 1.7398 upper-bound construction places its
multiples. That content is in the paper, not in this note. Until the PDF text is on
disk, the honest ceiling for any claim about the paper's method is CITED.
