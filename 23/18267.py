def f(x,y,z):
    if x==y:
        return 1
    if x>y :
        return 0
    if x<y:
        if z[-1]=="C":
            return f(x + 2, y, "A") + f(x + 5, y, "B")
        else:
            return f(x+2,y,z+"A")+f(x+5,y,z+"B")+f(x**2,y,z+"C")
print(f(4,36," "))