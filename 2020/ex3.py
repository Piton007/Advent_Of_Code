map = []

def move(origin,slope):
    return [origin[0]+slope[0],origin[1]+slope[1]]

def trees_by_slope(mov):
    trees = 0
    y0,x0 = [0,0]
    limit = len(map) - 1
    while limit > 0:
        y1, x1 =  y0+ mov[0], x0 + mov[1]
        if x1 >= len(map[0]):
            x1 = x1 - len(map[0])
        y0 , x0 = y1,x1 
        if map[y0][x0] == 1:
            trees = trees + 1 
        limit = limit - mov[0]
    return  trees


with open("ex3.txt","r") as file:
    for line in file:
        row = []
        for c in line.strip():
            if c == ".":
                row.append(0)
            if c == "#":
                row.append(1)
        map.append(row)



slopes =  [(1,1),(1,3),(1,5),(1,7),(2,1)]



result = 1


for slope in slopes:
    result = result * trees_by_slope(slope)
print(result)




