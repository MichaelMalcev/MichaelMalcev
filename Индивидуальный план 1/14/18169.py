def f(n,ss):
    s=0
    while n!=0:
        v=n%ss
        if v==0:
            s += 1
        n //= ss
    return s
for x in range(100000):
    b=3**2000 + 3**10 - x
    a=str(f(b,3))
    if a.count("2")==2000:
        print(x)
