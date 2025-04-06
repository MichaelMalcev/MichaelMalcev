from string import ascii_lowercase

alph="0123456789"+ascii_lowercase
for x in alph[:19]:
    a=int("98" + x + "79641", 19)
    b=int("36" + x + "14", 19)
    c=int("73" + x + "4", 19)
    d=a+b+c
    if d%18==0:
        print(d/18,x)
