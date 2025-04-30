for a in range(0,1000):
    flag=True
    for x in range(0,1000):
        for y in range(0,1000):
            f=(5<y) or (x>32) or (x+2*y<a)
            if f==0:
                flag=False
                break
    if flag==True:
        print(a)