p=open("20282.txt")
c=0
for i in p:
    a=[int(x) for x in i.split()]
    a_povt=[x for x in a if a.count(x)==3]
    a_razl=[x for x in a if a.count(x)==1]
    if len(a_povt)==3 and len(a_povt)==3:
        if (max(a)**2 + min(a)**2) >= ((sum(a)-max(a)-min(a))**2):
            c+=1
print(c)