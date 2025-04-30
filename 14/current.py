p=[]
def f(n,ss):
    s=""
    while n>0:
        s+=str(n%ss)
        n//=ss
    return s[::-1]
for x in range(1,1951):
    a=f(72070+7400-x,9)
    p.append(a.count("0"))
print(max(p))


































































# from string import ascii_lowercase
# alph="0123456789"+ascii_lowercase
#
# for y in range(7,36):
#     for x in alph[:y]:
#         a=int("4163"+x+"1",y)
#         b=247393
#         if a==b:
#             print(x,y)