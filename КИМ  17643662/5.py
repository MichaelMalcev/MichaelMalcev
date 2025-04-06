p=[]
for n in range(2,1000):
    b = bin(n)[2:]
    z=b[0:2]
    b= b + z[1] +z[0]
    r=int(b,2)
    if r>74:
        p.append(n)
print(min(p))