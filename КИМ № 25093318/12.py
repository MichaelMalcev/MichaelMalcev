for n in range(4,1000):
    s="3"+"1"*n
    while "31" in s or "211" in s or "1111" in s:
        if "31" in s:
            s=s.replace("31","1",1)
        if "211" in s:
            s=s.replace("211","13",1)
        if "1111" in s:
            s=s.replace("1111","2",1)
    a=s.count("1")+s.count("3")*3+s.count("2")*2
    if a==15:
        print(n)
        break

