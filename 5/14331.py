p=[]
def f(n,ss):
    g=""
    while n>0:
        g+=str(n%ss)
        n//=ss
    return g[::-1]
for n in range(1,1000):
    b=f(n,3)
    s=(b.count("1")+b.count("2")*2)
    if s%3==0:
        b=b+"212"
    elif s%3!=0:
        b=b+f(s*2,3)
    r=int(b,3)
    if r>490:
        p.append(r)
print(min(p))