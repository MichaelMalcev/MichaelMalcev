for x in "013456789abcde":
    a = int("1" + x + "51", 15)
    b = int("3" + x + "2", 15)
    c = a - b
    if c%4==0:
        print (c//4)