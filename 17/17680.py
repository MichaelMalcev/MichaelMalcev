p=open("17_17680.txt")
l=[]
a=[int(x) for x in p]
k_tt=min([x for x in a if x%41==0 and x>0])
c=0
for i in range(len(a)-1):
    k=[a[i],a[i+1]]
    if a[i]!=a[i+1]:
        if abs(a[i]-a[i+1])%k_tt==0:
            l.append(a[i]+a[i+1])
            c+=1
print(c,max(l))