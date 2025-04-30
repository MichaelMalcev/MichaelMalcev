from itertools import *
n=0
p=product("0123456789abc",repeat=3)
c=-1
for i in p:
    a="".join(i)
    a=a.replace("1","*")
    a=a.replace("3","*")
    a=a.replace("5","*")
    a=a.replace("7","*")
    a=a.replace("9","*")
    a=a.replace("b","*")
    if a[0]!="0":
        c+=1
        if "**" not in a:
            if str(c)[-1] == "7":
                n += 1
print(n)

