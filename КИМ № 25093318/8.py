from itertools import *
c=0
p=product(sorted("ДГИАШЭ"),repeat=5)
for i in p:
    i="".join(i)
    i=i.replace("А","*")
    i=i.replace("И","*")
    i=i.replace("Э","*")
    i=i.replace("Д","#")
    i=i.replace("Г","#")
    i=i.replace("Ш","#")
    if i[0]!="*" and i[-1]!="#":
        c+=1
print(c)