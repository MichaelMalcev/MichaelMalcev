for n in range (2,1000):
    h = str(n)
    a=0
    for p in h:
        if int(p)%2==0:
            a+=int(p)
    l=list(h)
    m=0
    for k in l[1::2]:
        m+=int(k)
        if len(l)==1:
            m=0
    r= abs(a-m)
    if r==13:
        print(n)
