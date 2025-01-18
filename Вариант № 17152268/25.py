from fnmatch import  fnmatch
def f(n):
    s=0
    d=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            d.add(i)
            d.add(n//i)
            s+=2
    return(s)
p=[]
for i in range(2031,10**9,2031):
    for z in range(0,20):
        x=f(i)
        if fnmatch(str(i),"*31*65?") and i%31==0 and x==2**z:
            p.append(i)
            p.append(i//2031)
print(p)

