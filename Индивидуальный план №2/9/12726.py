p=open("12726.txt")
c=0
for i in p:
    c+=1
    a=sorted([int(x) for x in i.split()])
    a_povt=[x for x in a if a.count(x)==3]
    a_razl=[x for x in a if a.count(x)==1]
    a_chet=[x for x in a if x%2==0]
    a_nechet=[x for x in a if x%2!=0]
    if len(a_povt)==3 and len(a_razl)==4:
        if len(a_chet) > len(a_nechet) :
            print(c)