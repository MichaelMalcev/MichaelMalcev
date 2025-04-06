a = 5 * 343**2031+4*49**2142-3*7**111 +7**222

def f(n,ss):
    s=0
    while n!=0:
        s += n % ss
        n //= ss
    return s
print(f(a,7))