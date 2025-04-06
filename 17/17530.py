p=open("17_17530.txt")
l=[]
a=[int(x) for x in p]
k_tt=min(a)
c=0
for i in range(len(a)-1):
    k=[a[i],a[i+1]]
    if a[i]%55==k_tt or a[i+1]%55==k_tt:
        c+=1
        l.append(a[i]+a[i+1])
print(c,min(l))