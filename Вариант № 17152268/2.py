for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((z <= w) or (y == w)) and ((x or z) == y)
                if f == 1:
                    print(z,y,x,w)