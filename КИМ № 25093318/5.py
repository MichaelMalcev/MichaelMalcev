p=[]
for n in range(2,1000):
    b=bin(n)[2:]
    if b.count("1")%2==0:
        b="10"+b[2:]+"0"
    elif b.count("1")%2!=0:
        b = "11" + b[2:] + "1"
    r=int(b,2)
    if r>480:
        p.append(n)
print(min(p))