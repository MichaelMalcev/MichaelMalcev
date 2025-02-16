p=[]
for n in range(1,1000):
    b=bin(n)[2:]
    b=str(b)
    b = b.replace("0", "a")
    b = b.replace("1", "0")
    b = b.replace("a", "1")
    b = "1" + b
    if b.count("1")%2==0:
        b= b+"0"
    if b.count("1")%2!=0:
        b= b+"1"
    r=int(b,2)
    if r>180:
        p.append(n)
print(min(p))