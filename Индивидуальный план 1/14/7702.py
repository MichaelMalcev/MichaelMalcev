from string import ascii_lowercase
alph = "0123456789"+ascii_lowercase
c=0

for x in alph[:18]:
    for y in alph[:18]:
        a=int("5" + x +"ga", 18)
        b=int("18" + x + "7", 18)
        if a+b:
            c+=1
print(c)