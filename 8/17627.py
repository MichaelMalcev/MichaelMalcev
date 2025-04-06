from itertools import *

a = product("0123456789abcde", repeat=5)
c=0
for i in a:
    word=''.join(i)
    if word[0]!="0":
        if  word.count('8')==1:
            word=word.replace('a',"*",1)
            word=word.replace('b',"*",1)
            word=word.replace('c',"*",1)
            word=word.replace('d',"*",1)
            word=word.replace('e',"*",1)
            if word.count('*')>=2:
                c+=1
print(c)
