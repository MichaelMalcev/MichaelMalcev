p=[]
def f(n,s):
    g=0
    h=0
    for i in n[-1::-1]:
        g+=i*s**h
        h+=1
    return g
for x in range(0,42):
    a=f([int("j",36),5,6,9,x],42)
    b=f([1,x,int("i",36),int("a",36)],42)
    c=a+b
    if c%155==0:
        p.append(x)
        print(x,c/155)
