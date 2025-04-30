p=open("27A_20295 (1).txt")
data=[list(map(float,x.split())) for x in p]
r=0.5

def calc_distane(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

def get_claster(x,y):
    claster=[dot for dot in data if calc_distane(x,y,dot[0],dot[1])<r]
    if len(claster)>0:
        for dot in claster:
            data.remove(dot)
        next_claster = [get_claster(dot[0],dot[1]) for dot in claster]
        claster = claster + sum(next_claster,[])
    return claster

while len(data)>0:
    dot=data.pop()
    current_claster=get_claster(dot[0],dot[1])
    print(len(current_claster))