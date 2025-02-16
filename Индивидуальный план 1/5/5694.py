p=[]
for n in range(1,1000):
    m=bin(278)[2:]
    m=str(m)
    b=bin(n)[2:]
    b=str(b)
    z=len(m)
    b="0"*z+b
    r=m or b
    if r.count("1")==7:
        p.append(n)
print(min(p))