def f(n):
    s = []
    while n != 0:
        s.append(n % 6)
        n //= 6
    return s[::-1]

p=[]
for x in range(1,2031):
    b = 6**260+6**160+6**60-x
    s = f(b)
    d = s.count(0)
    if d == 202:
        p.append(x)
print(max(p))



