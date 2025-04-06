p=[]
def f(n,ss):
    s=""
    while n>0:
        s+= str(n%ss)
        n//=ss
    return s[::-1]
for n in range(2,1000,2):
    b=f(n,3)
    if n%3==0:
        b=b+b[-2:]
    elif n%3!=0:
        b=b+f((b.count("1")+b.count("2")*2),3)
    r=int(b,3)
    if r>220:
        p.append(r)
print(min(p))