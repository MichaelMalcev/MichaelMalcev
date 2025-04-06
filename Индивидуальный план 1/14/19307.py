def f(n,ss):
    s=""
    while n!=0:
        s += str(n%ss)
        n//=ss
    return s[::-1]
a=15625**16-(3125**3) * 25**19 + 625**4 - 2005
b=str(f(a,5))
print(b.count("0"))