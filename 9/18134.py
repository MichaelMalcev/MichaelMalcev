p=open("18134.txt")
c=0
for i in p:
    a=[int(x) for x in i.split()]
    a_povt=[x for x in a if a.count(x)==2]
    a_razl=[x for x in a if a.count(x)==1]
    if len(a_povt)>=2:
        a_kv=max(a_povt)
    else:
        continue
    if len(a_povt)==4 and len(a_razl)==2 and a_kv**2> a_razl[0]*a_razl[1]:
        c+=1
print(c)
