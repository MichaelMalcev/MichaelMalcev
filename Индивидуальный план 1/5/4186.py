p=[]
for n in range(1,1000):
    b=bin(n)[2:]
    b=str(b)
    if n%2==0:
        b = b + "10"
    if n%2!=0:
        b = "1"+ b +"01"
    r=int(b,2)
    if r>441:
        p.append(n)
print(min(p))