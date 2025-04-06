def mod(m,n):
    return m%n
for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        f=(a + x > 700 - a) and (mod(a,100) + mod(100,x)>50)
        if f==0:
            flag = False
            break
    if flag == True:
        print(a)