p=[]
def f(n,ss):
    s=""
    while n>0:
        s+=str(n % ss)
        n//=ss
    return s[::-1]
for n in range(4,1000):
    b=f(n,3)
    if (b.count("1")+b.count("2")*2)%2==0:
        b="12"+b[2:]+"0"
    elif (b.count("1")+b.count("2")*2)%2!=0:
        b="10"+b[2:]+"2"
    r=int(b,3)
    if r>105:
        p.append(n)
print(min(p))