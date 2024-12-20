n = 1000000
z=[]
for i in range(1,n//2+1):
    if n%i==0:
        z.append(i)
print(z)
