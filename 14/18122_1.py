p=[]
def f(n):
    s=[]
    while n>0:
        s.append(n%5)
        n//=5
    return s
for x in range(1,5556):
    v=5**150 + 5**135 - x
    a=f(v)
    if a.count(4)==134:
        p.append(x)
print(max(p))