p=open("26 (9).txt")
a=sorted([int(x) for x in p])
b=a[0:2500]
c=sum(b)*0.5 + sum(a[-7500:])
print(c)