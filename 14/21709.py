def f(n,ss):
    s=""
    while n>0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
z=0
for x in range(1,3000):
    a=f((4**210+4**110-x),4)
    n=a.count("0")
    if n>z:
        z=n
    if n==105:
        print(x)
print(z)