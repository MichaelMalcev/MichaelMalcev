from math import prod
p=open("18364.txt")
c=0
for i in p:
    a=sorted([int(x) for x in i.split()])
    a_povt=[x for x in a if a.count(x)>1]
    a_razl=[x for x in a if a.count(x)==1]
    if len(a_povt)>0:
        if (sum(a_razl)*3) <= (prod(a_povt)):
            c+=1
print(c)