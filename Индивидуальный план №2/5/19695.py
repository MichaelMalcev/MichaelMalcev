p=[]
for n in range(4,1000):
    b=bin(n)[2:]
    if n%3==0:
        b=b+b[-2:]
    elif n%3!=0:
        b="1"+b+"1"
    r=int(b,2)
    if r>700:
        p.append(r)
print(min(p))