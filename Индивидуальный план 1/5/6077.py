p=[]
for n in range(100,1000):
    for m in range(100,1000):
        n =str(n)
        m =str(m)
        a =int(n[0])+int(m[0])
        b =int(n[1])+int(m[1])
        c =int(n[2])+int(m[2])
        r = str(c) + str(a) + str(b)
        g = r[-4:-1:]
        print(n,m)
        print(g,r)
        if g =="002":
            p.append(n,m)
print(p)
#не понятно почему не рабоатет. вроде все правильно.