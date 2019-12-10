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

def visible(grid, x, y, p, destroy = False):
    # given a grid of # and ., calculate visibility
    # from a given x and y
    count = 0
    j = x + p[0]
    i = y + p[1]
    while i>=0 and i<len(grid) and j>=0 and j<len(grid[i]):
        if grid[i][j] == "#":
            count += 1
            if destroy:
                grid[i][j] = "."
            break
        j += p[0]
        i += p[1]
    return count

grid = readData("day10-1.txt")
gridsize = len(grid)
print("max grid size is",gridsize)

offsets = []
# my code below doesn't handle the horiz and vert correctly
offsets.append((0,1,200))
offsets.append((1,0,100))
offsets.append((-1,0,300))
offsets.append((0,-1,0))
for j in range(1,gridsize):
    for i in range(1,gridsize):
        # only do 1/4 of the way around xy chart
        # we can add it mirrored for the other three quads
        if gcd(i,j) == 1:
            # calculate "radians" from the 12 o'clock
            if j == 0:
                sine = 0
            else:
                sine = 1.0 * i / j
            # y coord goes down the screen, not up
            offsets.append((i,j,200-sine))
            offsets.append((i,-j,sine))
            offsets.append((-i,-j,400-sine))
            offsets.append((-i,j,200+sine))
# sort the offsets by their "radians"
offsets.sort(key=lambda t: t[2])
print(len(offsets),"offsets")

counts = []
max = -1; maxX = -1; maxY = -1
for y in range(len(grid)):
    countLine = []
    for x in range(len(grid[y])):
        count = 0
        for p in offsets:
            count += visible(grid,x,y,p)
        if count > max:
            max = count
            maxX = x
            maxY = y
        countLine.append(count)
    counts.append(countLine)
print("Best view is",max, "at", maxX, maxY)
print("Obliterate them all!")
kills = 0
while kills < 200:
    for p in offsets:
        if visible(grid,maxX,maxY,p,True) == 1:
            kills += 1
            if kills % 50 == 0:
                print(kills, maxX+p[0], maxY+p[1])
