p=open("20189.txt")
c=0
for i in p:
    a=sorted([int(x) for x in i.split()])
    a_povt=[x for x in a if a.count(x)==2]
    a_razl=[x for x in a if a.count(x)==1]
    if len(a_povt)==4 and len(a_razl)==3:
        if a[0]*a[1]>sum(a[2:]):
            c+=1
print(c)


