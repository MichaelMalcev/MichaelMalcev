from string import ascii_uppercase
a=open("24_21421.txt").readline()
alph = ascii_uppercase
for i in alph[2:]:
    a = a.replace(i," ")
a=a.split()
a=[x.lstrip("0") for x in a]
l=0
for i in a:
    if len(i)>l and int(i,12)%2==0:
        l=len(i)
print(l)