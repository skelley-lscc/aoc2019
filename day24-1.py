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

def calcDiversity(mem):
    total = 0
    for j in range(5):
        for i in range(5):
            if mem[j][i] == "#":
                total += 2 ** (j * 5 + i)
                #print("...",total)
    return total

def neighbor(mem, j, i):
    count = 0
    for y in [j-1,j,j+1]:
        if y >= 0 and y <= 4:
            for x in [i-1,i,i+1]:
                if x >= 0 and x <= 4:
                    if (x == i or y == j) and (not (x==i and y==j)):
                        print(x,y)
                        if mem[y][x] == "#":
                            count += 1
    return count

def performStep(mem):
    newmem = []
    # make a local copy
    for L in mem:
        newmem.append(L[:])
    # calculate based on old copy
    for j in range(5):
        for i in range(5):
            n = neighbor(mem, j, i)
            print(j,i,n)
            if mem[j][i] == "#":
                if n == 1:
                    newmem[j][i] = "#"
                else:
                    newmem[j][i] = "."
            elif mem[j][i] == ".":
                if n < 1 or n > 2:
                    newmem[j][i] = "."
                else:
                    newmem[j][i] = "#"
    return newmem

def printGrid(mem):
    for L in mem:
        for I in L:
            print(I,end="")
        print()
    print(calcDiversity(mem))

mem = readTextData("day24-1.txt")
printGrid(mem)
biodiversity = []

bio = calcDiversity(mem)
while bio not in biodiversity:
    biodiversity.append(bio)
    mem = performStep(mem)
    printGrid(mem)
    bio = calcDiversity(mem)
print(biodiversity)
print("Duplicate bio is",bio)
