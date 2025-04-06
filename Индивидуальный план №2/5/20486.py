p=[]
for n in range(4,1000):
    b=bin(n)[2:]
    if n%2==0:
        b=b+b[:3]
    elif n%2!=0:
        b="1"+b+"01"
    r=int(b,2)
    if r>600:
        p.append(r)
print(min(p))