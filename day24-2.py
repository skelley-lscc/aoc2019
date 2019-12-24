from __future__ import print_function
# game of life variation
def parseTextLine(data):
    xmem = []
    for item in data:
        xmem.append(item)
    return xmem

def readTextData(filename):
    # read input file, build memory array
    xmem = []
    f = open(filename,"r")
    data = f.readline().strip()
    while len(data) > 0:
        newmem = parseTextLine(data)
        xmem.append(newmem)
        data = f.readline().strip()
    f.close()
    return xmem

def calcDiversity(mem,level):
    total = 0
    for j in range(5):
        for i in range(5):
            if mem[level][j][i] == "#":
                total += 2 ** (j * 5 + i)
                #print("...",total)
    return total

def neighbor(mem, level, j, i):
    count = 0
    for y in [j-1,j,j+1]:
        for x in [i-1,i,i+1]:
            if (x == i or y == j) and (not (x==i and y==j)):
                if y < 0:
                    #print("y<0:",j,i,y,x,mem[level-1][1])
                    if level-1 in mem and mem[level-1][1][2] == "#":
                        count += 1
                elif y > 4:
                    if level-1 in mem and mem[level-1][3][2] == "#":
                        count += 1
                elif x < 0:
                    if level-1 in mem and mem[level-1][2][1] == "#":
                        count += 1
                elif x > 4:
                    if level-1 in mem and mem[level-1][2][3] == "#":
                        count += 1
                else:
                    #print(x,y)
                    if x==2 and y==2 and level+1 in mem:
                    # oh dear, loop all the next layer bugs
                        if j == 1:
                            # top bugs
                            for k in range(5):
                                if mem[level+1][0][k] == "#":
                                    count += 1
                        if j == 3:
                            # bottom bugs
                            for k in range(5):
                                if mem[level+1][4][k] == "#":
                                    count += 1
                        if i == 1:
                            # left bugs
                            for k in range(5):
                                if mem[level+1][k][0] == "#":
                                    count += 1
                        if i == 3:
                            # right bugs
                            for k in range(5):
                                if mem[level+1][k][4] == "#":
                                    count += 1
                    elif mem[level][y][x] == "#":
                        count += 1
    return count

def performStep(mem, level):
    newmem = []
    # make a local copy
    for L in mem[level]:
        newmem.append(L[:])
    # calculate based on old copy
    for j in range(5):
        for i in range(5):
            n = neighbor(mem, level, j, i)
            #print(j,i,n)
            if mem[level][j][i] == "#":
                if n == 1:
                    newmem[j][i] = "#"
                else:
                    newmem[j][i] = "."
            elif mem[level][j][i] == ".":
                if n < 1 or n > 2:
                    newmem[j][i] = "."
                else:
                    newmem[j][i] = "#"
            if j == 2 and i == 2:
                # the middle of infinity is blank :)
                newmem[j][i] = "."
    return newmem

def printGrid(mem, level):
    for L in mem[level]:
        for I in L:
            print(I,end="")
        print()
    print(calcDiversity(mem,level))

xmem = readTextData("day24-1.txt")
mem = {}
mem[0] = xmem
printGrid(mem,0)
biodiversity = []
#print(mem)
bio = calcDiversity(mem,0)
count = 0
while count < 200:
    count += 1
    above = []
    below = []
    blankLine = ['.','.','.','.','.']
    for _ in range(5):
        above.append(blankLine[:])
        below.append(blankLine[:])
    mem[-count] = below
    mem[count] = above
    biodiversity.append(bio)
    newmem = {}
    for z in mem:
        newmem[z] = performStep(mem, z)
        print("Level",z)
        printGrid(newmem,z)
    #tt = raw_input("?")
    mem = newmem
    printGrid(mem,0)
    bio = calcDiversity(mem,0)
print(biodiversity)
#print("Duplicate bio is",bio)
print(mem)
bugCount = 0
for z in mem:
    for j in range(len(mem[z])):
        for i in range(len(mem[z][j])):
            if mem[z][j][i] == "#":
                bugCount += 1
print("Total bugs:",bugCount)
