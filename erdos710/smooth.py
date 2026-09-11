import sys
sys.path.insert(0,'oracle/evidence/erdos710')
from hall import min_violator
from e710 import f_unseeded
def lpf(m):
    p=2; best=1
    while p*p<=m:
        while m%p==0: best=p; m//=p
        p+=1
    return max(best,m)
print("n\tendpoint\t|T|\tmaxLPF(T)\tmaxLPF(U)\tminT\tmaxT")
for n in [20,30,40,50,64,72,80,90,100,108,120,128]:
    L=f_unseeded(n); T,U,a,b=min_violator(n,L-1)
    print(f"{n}\t{n+L}\t\t{a}\t{max(map(lpf,T))}\t\t{max(map(lpf,U))}\t\t{min(T)}\t{max(T)}")
print()
# Is T EXACTLY the y-smooth numbers in [minT, n]?
for n in [90,100,108,128]:
    L=f_unseeded(n); T,U,a,b=min_violator(n,L-1)
    y=max(map(lpf,T)); lo=min(T)
    full=[m for m in range(lo,n+1) if lpf(m)<=y]
    print(f"n={n} y={y} T has {len(T)}; all {y}-smooth in [{lo},{n}] = {len(full)}; T==that set? {sorted(T)==full}")
    if sorted(T)!=full: print("   missing from T:", [m for m in full if m not in T])
