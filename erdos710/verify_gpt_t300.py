import sys, os
sys.path.insert(0, os.path.join('oracle', 'evidence', 'erdos710'))
sys.setrecursionlimit(1000000)
from e710 import feasible
# GPT claims t(300)=510 inclusive => e710 convention f(300)=511
lo = feasible(300, 510)
hi = feasible(300, 511)
print("n=300 claimed f=511: feasible(510)=%s feasible(511)=%s -> %s" % (
    lo, hi, "CONFIRMED" if (not lo and hi) else "REFUTED"), flush=True)
