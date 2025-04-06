p=open("17_13088.txt")
l=[]
c=0
a=[int(x) for x in p]
s=max([x for x in a if str(x)[-2:]=="17"])
for i in range(len(a)-2):
    k=[a[i],a[i+1],a[i+2]]
    k_4=[x for x in k if len(str(x))==4]
    k_5=[x for x in k if x%5==0]
    if len(k_4)==2:
        if len(k_5)>=1:
            if sum(k)>s:
                l.append(sum(k))
                c+=1
print(c,max(l))