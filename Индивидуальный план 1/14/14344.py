from string import ascii_lowercase
alph="0123456789"+ascii_lowercase
for p in range(16,37):
    a=int("17496",p)
    b=int("91f83",p)
    c=int("d9543",p)
    d=a+b+c
    if d%12==0:
        print(d/12,p)