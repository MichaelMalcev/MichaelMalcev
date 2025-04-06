p=open("17_17558.txt")
l=[]
a=[int(x) for x in p]
k_tt=len([x for x in a if x%32==0])
c=0
for i in range(len(a)-1):
    k=a[i]+a[i+1]
    if a[i]<0 or a[i+1]<0:
        if a[i]+a[i+1]<k_tt:
            c+=1
            l.append(a[i]+a[i+1])
print(c,max(l))