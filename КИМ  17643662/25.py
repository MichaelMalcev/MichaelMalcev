def f(n):
    s=[]
    for i in range(1,int(n**0.5)):
        if n%i==0:
            s.append(i)
            s.append(n//i)
    return sorted(s)
for x in range(800000,850000):
    d=f(x)
    m=d[1]+d[-2]
    if str(m)[-1]=="4":
        print(x,m)
