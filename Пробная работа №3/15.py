p=[]
def DEL(n,m):
    if n%m==0:
        return 1
    else:
        return 0
for a in range(1,300):
    flag=True
    for x in range(0,1000):
        s=((not DEL(x, a)) and DEL(x, 35)) <= ((not DEL(x, 21)) or (not DEL(x, 35)))
        if s==0:
            flag=False
            break
    if flag==True:
        p.append(a)
print(max(p))
