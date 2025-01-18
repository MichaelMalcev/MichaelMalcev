p=[]
A=int()
for x in range(1,1000):
    f=((x&57 > 0) or (x&99 > 0)) <= (x&A > 0)
    while A>0:
        if f==1:
            p.append(A)
        print(p)

