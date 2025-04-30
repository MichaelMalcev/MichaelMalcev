p=open("17_21712.txt")
a=[int(x) for x in p]
c=0
n=0
d=[x for x in a if len(str(x))==4 and str(x)[-1]=="6" and x>0]
m=min(d)
for i in range(len(a)-2):
    s=[a[i],a[i+1],a[i+2]]
    g=sum(s)
    if (len(str(abs(s[0])))==4 and str(s[0])[-1]=="6") or (len(str(abs(s[1])))==4 and str(s[1])[-1]=="6") or (len(str(abs(s[2])))==4 and str(s[2])[-1]=="6"):
        if g<=m:
            c+=1
            if n<g:
                n=g
print(c,n)
