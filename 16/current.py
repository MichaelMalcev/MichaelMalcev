import sys
sys.setrecursionlimit(10**6)

p=[]

def f(n):
    if n==0:
        return 0
    if n>0 and n%2==0:
        return f(n/2)
    if n%2!=0:
        return 1+f(n-1)
# def g(n):
#     if n==1:
#         return 1
#     if n>=2:
#         return f(n-1)+g(n-1)
for n in range(0,10000):
    if f(n)==12:
        p.append(n)
print(min(p))