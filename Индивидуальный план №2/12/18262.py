for n in range(0,1000):
    s=">"+"0"*17+"3"*n+"2"*17
    while ">3" in s or ">2" in s or ">0" in s:
        if ">3" in s:
            s=s.replace(">3","22>",1)
        if ">2" in s:
            s=s.replace(">2","2>",1)
        if ">0" in s:
            s=s.replace(">0","3>",1)
    if (s.count("3")*3+s.count("2")*2)==121:
        print(n)