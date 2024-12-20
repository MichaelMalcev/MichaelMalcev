def f(n,ss):
    s=""
    while n!=0:
        s += str(n%ss)
        n//=ss
    return s[::-1]

b=[]

for x in range(1,5556):
    q = 5**150 + 5**135 - x
    z = f(q,5)
    if z.count('4')==134:
        b.append(x)

print(max(b))