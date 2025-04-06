p=[]
def f(n,ss):
    s=""
    while n>0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
for n in range(4,1000):
    b=f(n,4)
    if n%4==0:
        b="2"+b+"03"
    elif n%4!=0:
        b=b+f((n%4)*5,4)
    r=int(b,4)
    if r<567:
        p.append(n)
print(max(p))