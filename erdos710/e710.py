import sys
sys.setrecursionlimit(1000000)

def feasible(n,L):
    """True iff (n, n+L) contains distinct a_1..a_n with k | a_k."""
    lo,hi=n+1,n+L-1
    if hi-lo+1 < n: return False
    adj=[]
    for k in range(1,n+1):
        s=((lo+k-1)//k)*k
        if s>hi: return False
        adj.append(list(range(s,hi+1,k)))
    order=sorted(range(n),key=lambda i:len(adj[i]))
    matchR={}
    def try_k(i,seen):
        for v in adj[i]:
            if v in seen: continue
            seen.add(v)
            if v not in matchR or try_k(matchR[v],seen):
                matchR[v]=i; return True
        return False
    for i in order:
        if not try_k(i,set()): return False
    return True

def f_unseeded(n):
    L=n+1
    while not feasible(n,L): L+=1
    return L

def forced_deficit(n,L):
    """Hall deficit over indices with exactly one multiple in the carrier."""
    lo,hi=n+1,n+L-1
    forced={}
    for k in range(1,n+1):
        s=((lo+k-1)//k)*k
        if s>hi: return None,None,None
        if s+k>hi: forced[k]=s
    vals=set(forced.values())
    return len(forced), len(vals), len(forced)-len(vals)

if __name__=='__main__':
    N=int(sys.argv[1]) if len(sys.argv)>1 else 120
    vals=[]
    for n in range(1,N+1):
        v=f_unseeded(n)
        vals.append(v)
        nf,nv,dfc=forced_deficit(n,v)
        print(f"{n}\t{v}\t{v-n}\tforced={nf}\tdistinct={nv}\tdeficit={dfc}",flush=True)
    desc=[(i+2,vals[i],vals[i+1]) for i in range(len(vals)-1) if vals[i+1]<vals[i]]
    print("DESCENTS",desc)
    print("MONOTONE_NONDECREASING",len(desc)==0)
