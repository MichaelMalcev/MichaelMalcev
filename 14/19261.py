def f(n,ss):
    s=[]
    h=0
    for i in n[::-1]:
        s.append(i*ss**h)
        h+=1
    return sum(s)
for x in range(37):
    # a=1*37**0+3*37+x*37**2+8*37**3+9*37**4
    # b=4*37**0+2*37+9*37**2+x*37**3+1*37**4
    a=f([9, 8, x, 3, 1],37)
    b=f([1, x, 9, 2, 4],37)
    c=a+b
    if c%21==0:
        print(c/21,x)