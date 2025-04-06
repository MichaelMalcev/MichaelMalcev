f = open("24 (1).txt").readline()`
s=""
p=[]
for i in f:
    s+=i
    if s[-2:]=="KL":
        p.append(len(s)-1)
        s=""
        s+="L"
    elif s[-2:]=="LK":
        p.append(len(s)-1)
        s=""
        s+="K"
print(max(p))