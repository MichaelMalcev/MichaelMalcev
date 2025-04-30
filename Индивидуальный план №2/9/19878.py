p=open("19878.txt")
c=0
for i in p:
    a=sorted([int(x) for x in i.split()])
    a_povt=[x for x in a if a.count(x)==3]
    a_razl=[x for x in a if a.count(x)==1]
    if len(a_povt)==3 and len(a_razl)==4:
        if sum(a_razl)/len(a_razl) <= max(a_povt):
            c+=1
print(c)