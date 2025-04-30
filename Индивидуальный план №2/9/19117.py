p=open("19117.txt")
c=0
for i in p:
    a=sorted([int(x) for x in i.split()])
    a_povt=[x for x in a if a.count(x)==2]
    a_razl=[x for x in a if a.count(x)==1]
    a_chet=[x for x in a if x%2==0]
    a_nechet=[x for x in a if x%2!=0]
    if (len(a_povt)==2 and len(a_razl)==3) or ((sum(a_chet)>sum(a_nechet)) and (len(a_chet)>0 and len(a_nechet)>0)):
            c+=1
print(c)