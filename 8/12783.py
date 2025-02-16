from itertools import *

a= permutations("0123456789", r=7)
c=0

for i in a:
    num = "".join(i)
    if num[0]!="0":
        for j in "02468":
            num=num.replace(j,"*")
        for l in "13579":
            num=num.replace(l,"#")
        if "**" not in num and "##" not in num:
            c+=1
print(c)