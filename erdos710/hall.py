import sys
sys.path.insert(0,'oracle/evidence/erdos710')
from e710 import f_unseeded, feasible
sys.setrecursionlimit(1000000)

def sets(n,L):
    lo,hi=n+1,n+L-1
    S={}
    for k in range(1,n+1):
        s=((lo+k-1)//k)*k
        S[k]=set(range(s,hi+1,k)) if s<=hi else set()
    return S

def min_violator(n,L):
    """Find a minimal (by greedy shrink) Hall violator: T with |union| < |T|."""
    S=sets(n,L)
    # find violated set via deficiency version of matching: use Konig from max matching
    adj={k:sorted(S[k]) for k in S}
    matchR={}; matchL={}
    def try_k(i,seen):
        for v in adj[i]:
            if v in seen: continue
            seen.add(v)
            if v not in matchR or try_k(matchR[v],seen):
                matchR[v]=i; matchL[i]=v; return True
        return False
    unmatched=[]
    for i in sorted(adj,key=lambda x:len(adj[x])):
        if not try_k(i,set()): unmatched.append(i)
    if not unmatched: return None
    # Konig: from an unmatched left vertex, alternating reachable set Z
    u=unmatched[0]
    Zl={u}; Zr=set(); stack=[u]
    while stack:
        i=stack.pop()
        for v in adj[i]:
            if v not in Zr:
                Zr.add(v)
                j=matchR.get(v)
                if j is not None and j not in Zl:
                    Zl.add(j); stack.append(j)
    T=sorted(Zl); U=set()
    for k in T: U|=S[k]
    return T,sorted(U),len(T),len(U)

for n in [30,50,64,90,100,108,120,128]:
    L=f_unseeded(n)
    r=min_violator(n,L-1)
    T,U,a,b=r
    print(f"n={n} endpoint={n+L} lastInfeasibleEndpoint={n+L-1}")
    print(f"   violator T (|T|={a}) = {T}")
    print(f"   union    (|U|={b}) = {U}")
    print(f"   deficit={a-b}")
    print()
