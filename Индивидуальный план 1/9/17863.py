p = open("19241.txt")
c=0
for i in p:
    c+=1
    a=[int(x) for x in i.split()]
    a_povt=[x for x in a if a.count(x)==3]
    a_razl=[x for x in a if a.count(x)==1]

    if len(a_povt)==6 and len(a_razl)==1:
        if sr<a_razl[0]:
            print(c,a)