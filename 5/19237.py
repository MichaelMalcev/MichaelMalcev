l=[]

def f(n):
    s=""
    while n>0:
        s = str(n%3)+s
        n//=3
    return s
for n in range(1,1001,):
    s=f(n)
    if n%3==0:
        s=s+s[-2]+s[-1]
    if n%3!=0:
        p=sum(map(int,list(s)))
        p=f(p)
        s=s+p
    r=int(s,3)
    if r%2==0 and r>220:
        l.append(r)
print(min(l))
