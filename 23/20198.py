def f(x, y, z):
    if x > y+2:
        return 0
    if x == y:
        return 1
    if x <= y+2:
        if z[-2:] == "AA":
            return f(x + 5, y, z + "B") + f(x * 2, y, z + "C")
        else:
            return f(x - 1, y, z + "A") + f(x + 5, y, z + "B") + f(x * 2, y, z + "C")
print(f(5,34,""))