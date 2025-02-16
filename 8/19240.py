from itertools import *

a = product("АВНРЬЯ",repeat=5)
c=0

for i in a:
    c+=1
    word = "".join(i)
    if word[0]!="Я" and word.count("Ь")<=1 and "ЯЯ" not in word:
        print(c, word)
