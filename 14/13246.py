from string import ascii_lowercase

alph = "0123456789" + ascii_lowercase

for p in range(10,37):
    for x in alph[:p]:
        for y in alph[:p]:
            a = int("24" + x + "9", p)
            b = int(y + x + y + "3", p)
            c = int(x + "4" + y + "0", p)
            if a+b==c:
                print(int(x+y+y,p))
