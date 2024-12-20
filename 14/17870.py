def f(n, ss):
    s=""
    while n!=0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]

b=[]

for x in range(1,2031):
    q = 7**170+7**100-x
    z = f(q,7)
    if z.count("0")==71:
        b.append(x)
print(max(b))
