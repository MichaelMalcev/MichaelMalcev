p=open("14253.txt")
c=0
for i in p:
    a=sorted([int(x) for x in i.split()])
    a_povt=[x for x in a if a.count(x)==2]
    a_razl=[x for x in a if a.count(x)==1]
    if (len(a_povt)==6 and len(a_razl)==1) or ((sum(a)/len(a))**0.5==int((sum(a)/len(a))**0.5)):
        c+=1
print(c)