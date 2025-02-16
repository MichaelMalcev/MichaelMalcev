p=[]
for n in range(2,1000,2):
    b=bin(n)[2:]
    if n%3==0:
        b = "1" + b[:-2] + "11"
    if n%3!=0:
        b = "10"+ b +"0"
    r=int(b,2)
    if r>999:
        p.append(r)
print(min(p))