a=3*3125**9+2*625**8-4*625**7+3*125**6-2*25**5-2024
def f(n,ss):
    s=0
    while n!=0:
        b=n%ss
        if b==0:
            s += 1
        n //= ss
    return s
print(f(a,25))