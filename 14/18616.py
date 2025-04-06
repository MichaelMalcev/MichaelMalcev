def f(n: list[int]):
    g = 0
    h = 0
    for i in n[::-1]:
        g += i * 37 ** h
        h += 1
    return g


for x in range(37):
    a = f([12, 5, 9, x, 11, 10, 9, 8, 15])
    b = f([int("e", 36), 3, x, 5, int("d", 36), 10, 9, 12, 6])
    c = a * b
    if c % 36 == 0:
        print(f([2, x, 1]))