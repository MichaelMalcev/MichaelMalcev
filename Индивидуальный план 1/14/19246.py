from string import ascii_lowercase
alph="0123456789" + ascii_lowercase
for i in range(1,26):
    for x in alph[:i]:
        a = int("11353" + x + "12",25)
        b = int("135" + x + "21",25)
        c = a + b
        if c%24==0:
            print(c/24)