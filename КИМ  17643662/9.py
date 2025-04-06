p=open("9.txt")
c=0
for i in p:
    a=[int(x) for x in i.split()]
    a_povt=[x for x in a if a.count(x)==2]
    a_razl=[x for x in a if a.count(x)==1]
    sr1=sum(a_povt)/2
    sr2=sum(a_razl)/4
    if len(a_povt)==2 and len(a_razl)==4:
        if sr1<sr2:
            c+=1
print(c)