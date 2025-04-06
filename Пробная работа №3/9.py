p=open("9.txt")
c=0
for l in p:
    a=[int(x) for x in l.split()]
    a_povt=[x for x in a if a.count(x)==2]
    a_razl=[x for x in a if a.count(x)==1]
    if len(a_povt)==4 and len(a_razl)==3:
        if sum(a_povt)/4<sum(a)/7:
            c+=1
print(c)