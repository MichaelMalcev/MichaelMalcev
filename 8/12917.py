from itertools import *

a = permutations("ПРОСТО", r=6)
c=0

for i in a:
    word="".join(i)
    if "ОО" not in word:
        c+=1
print(c//2)