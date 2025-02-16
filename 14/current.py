a = 9**8+3**5-9
def f(n):
    s=[]
    while n>0:
        s.append(n%3)
        n//=3
    return s[::-1]
b=f(a)
c=b.count(2)
print(c)