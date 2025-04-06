f = open("24 (5).txt").readline()

c_t = 0
s = ""
list_lens = []

for i in f:
    s += i
    if s.count("T") == 101:
        list_lens.append(len(s) - 1)
        s = s[s.index("T") + 1: ]

print(max(list_lens))