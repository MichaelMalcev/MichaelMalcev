def f(n,s):
    g=0
    h=0
    for i in n[::-1]:
        g+=i*s**h
        h+=1
    return g
for x in range(67):
    a=f([3, x, 2, 1],81)
    b=f([1, 7, x, 4],67)
    c=a+b
    if c%35==0:
        print(c/35)

