import sys
sys.setrecursionlimit(10**6)
def f(n):
    if n<110:
        return n
    if n>=110:
        return n+f(n-1)
print(f(2025)-f(2021))