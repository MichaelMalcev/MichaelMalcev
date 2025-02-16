p = open("19228.txt")

c=0

for i in p:
    a = [int(x) for x in i.split()]
    a_povt = [x for x in a if a.count(x)==4]
    a_razl = [x for x in a if a.count(x)==1]
    if len(a_povt)==4 and len(a_razl)==2:
        if a_povt[0]**2 < sum(a_razl):
            c+=1
print(c)