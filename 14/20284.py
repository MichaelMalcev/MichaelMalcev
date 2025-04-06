def f(n):
    g=0
    h=0
    for i in n[::-1]:
        g+= i*42**h
        h+=1
    return g
for x in range(42):
    a=f([int("j",36),5,6,9,x])
    b=f([1,x,int("i",36),int("a",36)])
    c=a+b
    if c%155==0:
        print(c/155)