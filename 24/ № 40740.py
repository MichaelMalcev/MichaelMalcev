f = open("24 (2).txt").readline()
s=""
p=[]
for i in f:
    s+=i
    if s.count("E")>=3 and s[-1]=="A":
        p.append(len(s)-1)
        s=""
    elif s[-1]=="A":
        s=""
print(max(p))