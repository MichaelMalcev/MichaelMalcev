#Мое # 8200 970
# w=[]
# p=open("26_demo (3).txt")
# a=sorted([int(x) for x in p])
# c=0
# s=0
# for i in range(len(a)):
#     if s+a[i]<=8200:
#         s+=a[i]
#         c+=1
#     else:
#         break
# for i in range(len(a)-1,-1,-1):
#     k=s-a[568]
#     if k+a[i]<=8200:
#         w.append(a[i])
# print(c,max(w))

# 8200 970
w=[]
p=open("26_demo (3).txt")
a=sorted([int(x) for x in p])
s = []
for i in range(len(a)):
    if sum(s)+a[i]<=8200:
        s.append(a[i])
    else:
        break
s.pop()
a.reverse()
for i in range(len(a)):
    if sum(s)+a[i]<=8200:
        s.append(a[i])
        break
print(len(s), max(s))