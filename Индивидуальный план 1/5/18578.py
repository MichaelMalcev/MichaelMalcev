p=[]
def f(n):
    s=""
    while n>0:
        s = str(n%4) + s
        n//=4
    return s
for n in range (1,1000):
    b=f(n)
    g=n%4
    if g==0:
        b="2" + b + "03"
    if g!=0:
        d=f(g*5)
        b = b + d
    r = int(b,4)
    if r<=567:
        p.append(n)
print(max(p))