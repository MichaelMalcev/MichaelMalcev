for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w == x) and (y <= z)
                g = (w <= x) <= (y == z)
                if f==0 and g==0:
                    print(x, y, z, w)