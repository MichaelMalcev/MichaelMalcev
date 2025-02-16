for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (z or w) and y and x
                if f==1:
                    print(x, y, z, w)