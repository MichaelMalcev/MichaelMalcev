from fnmatch import fnmatch
def f(n):
    z=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            z.add(i)
            z.add(n//i)
    return list(z)
for i in range(1,10**7):
    g=f(i)
    if fnmatch(str(i),"3?1111*") and g==[1,i]:
        print(i)
