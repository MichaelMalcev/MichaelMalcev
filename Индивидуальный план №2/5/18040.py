p=[]
for n in range(1,1000,2):
    b=bin(n)[2:]
    if n%5==0:
        b=b[:3]+b
    elif n%5!=0:
        b=b+bin((n%5)*5)[2:]
    r=int(b,2)
    if r<313:
        p.append(n)
print(max(p))