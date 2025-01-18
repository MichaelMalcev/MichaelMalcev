
def f (n):
    p=[]
    for i in range (1,int(n**0.5) + 1 ):
        if n%i==0:
            p.append(i)
            p.append(n//i)
    return sorted(p)
v=[]
for i in range(800001, 800100):
    z=f(i)
    for x in z:
        g=str(x)
        if int(g[-1])==9 and x!=i and x!=9:
            v.append([i,x])
            break
    print(v)
