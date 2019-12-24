from __future__ import print_function
# to check all possible visible lanes:
# generate all possible a/b fractions
# if the fraction can reduce, it's already covered
# 1/2 ok, 2/3 ok, 5/7 ok, 3/9 covered
def gcd(a,b):
    if a == 0 or b == 0:
        # we want 1,0 or 0,1 but not 3,0 or 0,4
        return abs(b-a)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def readData(filename):
    grid = []
    f = open(filename,"r")
    line = f.readline().strip()
    while len(line) > 0:
        gridLine = []
        for c in line:
            gridLine += c
        grid.append(gridLine)
        line = f.readline().strip()
    f.close()
    return grid

def visible(grid, x, y, p):
    # given a grid of # and ., calculate visibility
    # from a given x and y
    count = 0
    # do this four times, once per quadrant
    for px in (-p[0], p[0]):
        for py in (-p[1], p[1]):
            i = x + px
            j = y + py
            while i>=0 and i<len(grid) and j>=0 and j<len(grid[i]):
                if grid[i][j] == "#":
                    count += 1
                    break
                i += px
                j += py
    return count

grid = readData("day10-1.txt")
gridsize = len(grid)
print("max grid size is",gridsize)

offsets = []
for i in range(gridsize):
    for j in range(1,gridsize):
        if gcd(i,j) == 1:
            offsets.append((i,j))
print(offsets)
print(len(offsets),"offsets")

counts = []
max = -1; maxX = -1; maxY = -1
for x in range(len(grid)):
    countLine = []
    for y in range(len(grid[x])):
        count = 0
        for p in offsets:
            #print(x,y,p)
            count += visible(grid,x,y,p)
        if count > max:
            max = count
            maxX = x
            maxY = y
        countLine.append(count)
    counts.append(countLine)

print(max, maxX, maxY)
