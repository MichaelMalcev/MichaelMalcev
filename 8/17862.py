from itertools import *
c=0
a=product("0123456789ab",repeat=5)
for i in a:
    i="".join(i)
    if i.count("7")==1 and i[0]!="0":
        i=i.replace("9","*")
        i=i.replace("a","*")
        i=i.replace("b","*")
        if i.count("*")<=3:
            c+=1
print(c)