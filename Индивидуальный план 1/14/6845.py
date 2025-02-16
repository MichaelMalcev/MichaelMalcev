from string import ascii_lowercase
alph="0123456789" + ascii_lowercase
for p in range(8,37):
    for x in alph[:p]:
        for y in alph[:p]:
            a = int("1" + x + "77",p)
            b = int(x + x + "77",p)
            c = int(y + "0" + y + y,p)
            if a + b ==c:
                print(int(y+x+y+x,p))