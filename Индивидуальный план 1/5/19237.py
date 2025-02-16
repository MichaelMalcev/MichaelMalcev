p=[]
def f(n):
    s=""
    while n>0:
        s = str(n%3) + s
        n//=3
    return s
for n in range(1,1000):
    b=f(n)
    if n%3==0:
        b=b+b[-2:]
    if n%2!=0:
        b=b + f(sum(map(int,list(b))))
    r=int(b,3)
    if r>220 and r%2==0:
        p.append(r)
print(min(p))

