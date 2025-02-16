from itertools import *

a = product("БМНРЮ", repeat=6)
c=0
for i in a:
    c+=1
    word="".join(i)
    if word[0]!="М" and word.count("Р")>=2 and word.count("Ю")==0 and c%2!=0:
        print(c, word)