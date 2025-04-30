def f(n):
    d=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
    return list(d)
for i in range(700000, 1400000):
    s=f(i)
    g=[]
    for x in s:
        if x!=7 and x!=i and str(x)[-1::]=="7":
            g.append(x)
    if not g:
        continue
    print(i,min(g))

