def f(n,ss):
    s=[]
    while n>0:
        s.append(n%ss)
        n//=ss
    return s[::-1]
a=f((5*729**2024 + 3*243**1413-7*81**169-2*9**107+3017),27)
c=0
for i in a:
    if i%2==0 and i<=25:
        c+=i
print(c)