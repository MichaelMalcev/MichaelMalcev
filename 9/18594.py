f = open("18594.txt")
c = 0
for i in f:
    a = [int(x) for x in i.split()]
    a1_chet=[x for x in a if x%2==0]
    a1_nechet=[x for x in a if x%2!=0]
    if len(a1_chet)==len(a1_nechet):
        if (min(a)**2) <= (sum(a)-min(a)):
            c+=1
print(c)