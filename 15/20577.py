for a in range(1,10000):
    flag = True
    for x in range(1,10000):
        f=(x&a!=0) <= ((x&698==0) <= (x&321!=0))
        if f==0:
            flag=False
            break
    if flag==True:
        print(a)