for a in range(0,500):
    flag = True
    for x in range(0,500):
        for y in range(0,500):
            f = (2*x+y != 150) or (x < 50 or x >70) or (a>y)
            if f == 0:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(a)