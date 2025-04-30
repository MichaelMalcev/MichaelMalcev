def DEL(n,m):
    if n%m==0:
        return 1
for a in range(1,1000):
    flag=True
    for x in range(1,1000):
        f = DEL(x,a) or ((x>=60 and x<=80) <= (not(DEL(x,22))))
        if f==0:
            flag=False
            break
    if flag==True:
        print(a)