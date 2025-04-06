p=[]
def f(n,ss):
    s=""
    while n>0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
for x in range(401,1000):
    s=f(16**560 + 16**120 - x,16)
    if s.count("0")==442:
        p.append(x)
print(min(p))