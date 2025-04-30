p=open("24.23_19887.txt").readline()
a=[0,1,2,3,4,5,6,7,8,9]
for i in range(0,10,2):
    p=p.replace(str(i),"*")
for i in range(1,10,2):
    p=p.replace(str(i),"#")
while "**" in p or "##" in p:
    p=p.replace("**","* *")
    p=p.replace("##","# #")
p=p.split()
print(len(max(p,key=len)))