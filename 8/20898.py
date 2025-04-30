from itertools import *
c=0
p=product("012345678",repeat=5)
for i in p:
    a="".join(i)
    for x in range(1,8,2):
        a=a.replace(str(x),"*")
    if a[0]!="0" and a.count("0")==1 and "*0" not in a and "0*" not in a:
        c+=1
print(c)