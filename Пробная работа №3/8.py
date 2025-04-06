c=0
def f(n,ss):
    s=""
    while n>0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
for x in range(100000,999999):
    k=f(x,6)
    if k.count("2")==1:
        if "21" not in k or "23" not in k or "25" not in k or "27" not in k or "29" not in k:
            if "12" not in k or "32" not in k or "52" not in k or "72" not in k or "92" not in k:
                c+=1
print(c)