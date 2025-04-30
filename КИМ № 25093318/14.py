from string import ascii_lowercase
alph="0123456789"+ascii_lowercase
for x in alph[:21]:
    a=int("82934" + x + "2",21)
    b=int("2924" + x + x + "7",21)
    c=int("67564" + x + "8",21)
    d=a+b+c
    if d%20==0:
        print(d/20,x)