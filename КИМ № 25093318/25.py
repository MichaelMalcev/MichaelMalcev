def f(n):
    d=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    return list(d)
for i in range(1125000,2000000):
    s=f(i)
    g=[x for x in s if x!=7 and x!=i and str(x)[-1::]=="7"]
    if not g:
            continue
    print(i,min(g))