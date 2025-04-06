p=open("9156.txt")
for i in p:
    a=[int(x) for x in i.split()]
    s=min(a)+max(a)
    a=sorted(a)
    if s%3==0:
        if s%3==0:
            print(s)