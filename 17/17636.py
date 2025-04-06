p=open("17_17636.txt")
l=[]
a=[int(x) for x in p]
k_tt=max([x for x in a if len(str(abs(x)))==3 and str(x)[-1]=="3"])
for i in range(len(a)-2):
    k=[a[i],a[i+1],a[i+2]]
    k_t=[x for x in k if len(str(abs(x)))==3 and str(x)[-1]=="3"]
    if len(k_t)>=1 and sum(k)<k_tt:
        l.append(sum(k))
print(len(l),max(l))