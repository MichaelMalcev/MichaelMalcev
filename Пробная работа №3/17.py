p=open("17 .txt")
o=[]
c=0
a=[int(x) for x in p]
for i in range(0,len(a)-2):
    b=[x for x in a if len(str(x))==3 and str(x)[-1]=="5"]
    m=min(b)
    if len(str(a[i]))==3 or len(str(a[i+1]))==3:
        if (a[i]+a[i+1])%m==0:
            c+=1
            o.append(a[i]+a[i+1])
print(c,max(o))
