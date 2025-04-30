p=open("14254.txt")
c=0
for i in p:
    a=sorted([int(x) for x in i.split()])
    a_povt=[x for x in a if a.count(x)>1]
    a_razl=[x for x in a if a.count(x)==1]
    if (sum(a_razl) <= sum(a_povt)) or ((max(a)*min(a)) < (3*(sum(a)-max(a)-min(a)))):
        c+=1
print(c)