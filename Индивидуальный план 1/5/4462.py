p=[]
for n in range(2,1000):
    b=bin(n)[2:]
    b=str(b)
    b=b[1:]
    if b.count("1")%2==0:
        b = "10" + b
    if b.count("1")%2!=0:
        b = "1" + b[2:] + "0"
    r=int(b,2)
    if r<450:
        p.append(r)
print(min(p))