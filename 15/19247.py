for a in range(0,500):
    flag = True
    for x in range(1,500):
        for y in range(1,500):
            f=(x-3*y < a) or (y > 400) or (x > 56)
            if f==0:
                flag = False
                break
    if flag == True:
        print(a)