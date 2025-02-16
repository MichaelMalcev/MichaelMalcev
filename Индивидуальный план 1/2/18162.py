for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f = ((a <= b) == c) or d
                if f==0:
                    print(a, b, c, d)