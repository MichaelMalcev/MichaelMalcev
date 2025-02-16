p = open("18258.txt")

c = 0

for i in p:
    c+=1
    a = [int(x) for x in i.split()]
    a_sort=sorted(a)
    a_povt=[x for x in a if a.count(x)>=2 and sum(map(int,list(str(x))))%2==0]
    if a==a_sort and len(a_povt)!=0:
        print(c,a)