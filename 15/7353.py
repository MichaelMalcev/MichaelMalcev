def DEL(n,m):
    if n%m==0:
        return True
    else:
        return False
for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        f=DEL(x,a) or ((70<= x <=80)<= (not DEL(x,18)))
        if f==0:
            flag = False
            break
    if flag == True:
        print(a)