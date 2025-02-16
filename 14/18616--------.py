from string import ascii_lowercase
alph= "0123456789" + ascii_lowercase
def f(n):
    g=""
    h=0
    for i in n[-1::-1]:
        g+=str(i*37**h)
        h+=1
    return int(g)

for p in range(1,38):
    for x in alph[:p]:
        a= f("c59" + x +"ba98f")
        b= f("e3" + x +"5da9c6")
        c=a*b
        if c&36==0:
            print(f("2" + x + "1"))