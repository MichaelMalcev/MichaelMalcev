p=[]
for n in range(1,1000):
    b=bin(n)[2:]
    if b.count("1")%2==0:
        b="101"+b[3:]+"01"
    elif b.count("1")%2!=0:
        b="111"+b[3:]+"10"
    r=int(b,2)
    if r<385:
        p.append(n)
print(max(p))