p=open("24_18597.txt").readline()
while "&&" in p or ".." in p or " ." in p or " &" in p or " 0" in p or "& " in p or ". " in p:
    p=p.replace("&&"," ")
    p=p.replace(".."," ")
    p=p.replace("&."," ")
    p=p.replace(".&"," ")
    p=p.replace(" ."," ")
    p=p.replace(" &"," ")
    p=p.replace(" 0"," ")
    p=p.replace("& "," ")
    p=p.replace(". "," ")
p=p.split()
for i in p:
    i=i.split("&")
    if len(i)>=2:
        for x in i:
            if x.count(".")==1:
                print(i)