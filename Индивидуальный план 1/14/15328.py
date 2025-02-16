from string import ascii_lowercase
alph="0123456789" + ascii_lowercase
for i in range(1,28):
    for x in alph[:i]:
        a = int("123" + x + "24",27)
        b = int("135" + x + "78",27)
        c = a + b
        if c%26==0:
            print(c/26)