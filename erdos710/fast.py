import sys, math
sys.setrecursionlimit(1000000)
def feasible_fast(n,L):
    """Hopcroft-Karp style with adjacency by residue; returns True if perfect matching k=1..n."""
    lo,hi=n+1,n+L-1
    if hi-lo+1<n: return False
    adj=[]
    for k in range(1,n+1):
        s=((lo+k-1)//k)*k
        if s>hi: return False
        adj.append(list(range(s,hi+1,k)))
    order=sorted(range(n),key=lambda i:len(adj[i]))
    matchR={}
    for i in order:
        seen=set(); stack=[(i,iter(adj[i]))]; path=[]
        # iterative DFS augment
        def aug(u,seen):
            st=[(u,iter(adj[u]))]
            trail=[]
            while st:
                x,it=st[-1]
                adv=False
                for v in it:
                    if v in seen: continue
                    seen.add(v)
                    if v not in matchR:
                        trail.append((x,v))
                        for a,b in trail: matchR[b]=a
                        return True
                    st.append((matchR[v],iter(adj[matchR[v]])))
                    trail.append((x,v)); adv=True; break
                if not adv:
                    st.pop()
                    if trail: trail.pop()
            return False
        if not aug(i,set()): return False
    return True
def endpoint(n, lo_hint=None):
    L=lo_hint or n+1
    while not feasible_fast(n,L): L+=1
    return n+L
if __name__=='__main__':
    import json
    N=int(sys.argv[1]); step=int(sys.argv[2]) if len(sys.argv)>2 else 1
    out={}
    for n in range(20,N+1,step):
        E=endpoint(n)
        out[n]=E
        print(f"{n}\t{E}\t{E-n}\t{E/n:.4f}\t{math.log(E/n):.4f}",flush=True)
    json.dump(out,open('oracle/evidence/erdos710/ratios.json','w'))
