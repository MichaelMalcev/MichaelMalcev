p=open("19481.txt")
c=0
l=[]
for i in p:
    c+=1
    a=sorted([int(x) for x in i.split()])
    a_povt=[x for x in a if a.count(x)>1]
    a_razl=[x for x in a if a.count(x)==1]
    if len(a_povt)==0 and len(a_razl)==4:
        if (a[0] + a[3])**2 > (a[1]**3 + a[2]**3):
            l.append(c)
print(sum(l))