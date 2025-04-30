from itertools import *

p=product("АКМС",repeat=6)
n=0
for i in p:
    n+=1
    a="".join(i)
    a=a.replace("С","*")
    a=a.replace("М","*")
    a=a.replace("К","#")
    if "*" not in a and "##" not in a:
        print(n,a)