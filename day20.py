from __future__ import print_function
# 15 minutes over 24 hours for part 1 -- oh well

def readData(filename):
    grid = []
    f = open(filename,"r")
    # can't strip the spaces
    line = f.readline()[:-1]
    while len(line) > 0:
        gridLine = []
        for c in line:
            gridLine += c
        grid.append(gridLine)
        line = f.readline()[:-1]
    f.close()
    return grid

def buildPads(grid):
    # text file has blank borders and centers
    # find an alphanumeric and build a dictionary of points
    pads = {}
    # skip first and last line
    y = 1
    while y < len(grid)-1:
        x = 1
        while x < len(grid[y])-1:
            c = grid[y][x]
            if c.isalpha():
                location = (-1, -1)
                # where is the period?
                if grid[y-1][x] == '.':
                    # below entrance
                    name = grid[y][x]+grid[y+1][x]
                    location = (y-1,x)
                if grid[y+1][x] == '.':
                    # above entrance
                    name = grid[y-1][x]+grid[y][x]
                    location = (y+1,x)
                if grid[y][x-1] == '.':
                    # right of entrance
                    name = grid[y][x]+grid[y][x+1]
                    location = (y,x-1)
                if grid[y][x+1] == '.':
                    # left of entrance
                    name = grid[y][x-1]+grid[y][x]
                    location = (y,x+1)
                if location != (-1, -1):
                    pads[location] = name
            x += 1
        y += 1
    return pads

def nextSteps(grid, curr, path):
    # given a point in the maze, add all points adjacent
    # recursively to the path dictionary, with distance
    # from the (first) curr point
    # -- there's gotta be a better algorithm for this
    next = []
    y=curr[0]; x=curr[1]; step=path[curr]+1
    if grid[y][x-1] == '.':
        n=(y,x-1)
        if n not in path:
            next.append(n)
            path[n]=step
    if grid[y][x+1] == '.':
        n=(y,x+1)
        if n not in path:
            next.append(n)
            path[n]=step
    if grid[y+1][x] == '.':
        n=(y+1,x)
        if n not in path:
            next.append(n)
            path[n]=step
    if grid[y-1][x] == '.':
        n=(y-1,x)
        if n not in path:
            next.append(n)
            path[n]=step
    return next

def buildPaths(grid, pads):
    # using the "points nearby" function, build a dictionary
    # of points that are connected, and the length of the
    # path between them
    # -- omg, there's two dictionary entries for all points
    # except AA and ZZ... add a second dictionary for overflow
    # -- part two, the inner exits connect to the outer exits
    # recursively, gotta flag that
    paths = {}; paths2 = {}
    for p in pads:
        path = {}
        next = [(p[0],p[1])]
        path[next[0]] = 0
        while len(next) > 0:
            curr = next.pop(-1)
            more = nextSteps(grid, curr, path)
            for m in more:
                next.append(m)
        start = pads[p]
        #print(start,p,path)
        adjacent = {}
        for (y, x) in path:
            if (y,x) in pads:
                toPoint = pads[(y,x)]
                if path[(y,x)] > 0:
                    adjacent[toPoint] = path[(y,x)]
                #print((y,x),pads[(y,x)],path[(y,x)])
        #print(start,adjacent)
        if start in paths:
            paths2[start] = adjacent
        else:
            paths[start] = adjacent
    return [paths, paths2]

grid = readData("day20.txt")
pads = buildPads(grid)
paths = buildPaths(grid,pads)
#print(grid)
#print(pads)
print(paths[0])
print(paths[1])
# now there's just points and lengths to next points
# find AA, then find all the points it leads to, etc.
used = ['AA']   # prevent backtracking
# calculate the endpoints, and replace the endpoints with
# the new distance and endpoint -- if the new distance is
# shorter
root = paths[0]['AA']
while 'ZZ' not in root:
    print(used)
    this = []
    for p in root:
        if p not in used:
            this.append(p)
    for p in this:
        used.append(p)
        if p in paths[0]:
            next = paths[0][p]
            for n in next:
                nSize = root[p] + 1 + next[n]
                if n not in root or root[n] > nSize:
                    root[n] = root[p] + 1 + next[n]
        if p in paths[1]:
            next = paths[1][p]
            for n in next:
                nSize = root[p] + 1 + next[n]
                if n not in root or root[n] > nSize:
                    root[n] = root[p] + 1 + next[n]
print(root)
