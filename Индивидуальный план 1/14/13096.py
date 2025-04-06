def f(n,s):
    g=0
    h=0
    for i in n[::-1]:
        g+=i*s**h
        h+=1
    return g
for x in range(39):
    for y in range(39):
        a=f([5, 8, x, 7, 2, 3, y, 4, 9, ], 39)
        b=f([y,x],39)
        if a%38==0 and (b**0.5 == round(b**0.5)):
            print(b)