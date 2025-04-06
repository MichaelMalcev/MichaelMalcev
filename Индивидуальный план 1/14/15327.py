def f(n,ss):
    s=""
    while s!=0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
a=3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029
b=f(a,27)
c=0
for i in b:
    if int(i)>9:
        c+=1
print(c)