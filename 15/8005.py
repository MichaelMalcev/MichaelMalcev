for a in range(0,1000):
    flag=True
    for x in range(15,31):
        f = (x&29==0) or ((x&11==0)<= (not(x&a==0)))
        if f==0:
            flag=False
            break
    if flag==True:
        print(a)