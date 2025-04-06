p=open("8497.txt")
c=0
for i in p:
    a=[int(x) for x in i.split()]
    a_razl=[x for x in a if a.count(x)==1]
    if len(a_razl)==5:
        if (min(a)+max(a))*3>=(sum(a)-min(a)-max(a))*2:
            c+=1
print(c)