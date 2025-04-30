p=open("17.txt")
c=0
n=0
a=[int(x) for x in p]
t=sum([x for x in a if x<0])
for i in range(0,len(a)-2):
    k=[a[i],a[i+1],a[i+2]]
    m=max(k)*min(k)
    if m>t:
        c+=1
    if sum(k)>n:
        n=sum(k)
print(c,n)