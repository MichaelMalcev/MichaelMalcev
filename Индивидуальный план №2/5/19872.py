p=[]
def f(n,ss):
    s=''
    while n>0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
for n in range(1,1000):
    b=f(n,7)
    if n%2==0:
        b="52"+b+"1"
    elif n%2!=0:
        b=b[-1]+b[1:-1]+b[0]+"15"
    r=f(int(b,7),7)
    if len(str(r))==4:
        p.append(n)
print(max(p))