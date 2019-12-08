from __future__ import print_function

def readData(filename, width, height):
    # read input file, build memory array
    layers = []
    layer = []
    row = []
    f = open(filename,"r")
    data = f.readline().strip()
    w = 0
    h = 0
    while len(data) > 0:
        for item in data:
            if h == height:
                layers.append(layer)
                layer = []
                h = 0
            if w == width:
                h += 1
                layer.append(row)
                row = []
                w = 0
            row.append(int(item))
            w += 1
        data = f.readline().strip()
    f.close()
    return layers

data = readData("day8-1.txt",25,6)
print(data)
stats = []
image = []
minz = 9999
for z in range(len(data)):
    cz = 0
    co = 0
    ct = 0
    for y in range(len(data[z])):
        ct += data[z][y].count(2)
        co += data[z][y].count(1)
        cz += data[z][y].count(0)
    if cz < minz:
        minz = cz
        print("min",cz,co * ct)
    print(z,ct,co,cz)

def printImg(image):
    for i in image:
        for j in i:
            if j == 2:
                print(" ",end="")
            elif j == 1:
                print("+",end="")
            else:
                print("#",end="")
        print()
    print()

image = data[0][:]
for i in image:
    for j in i:
        print(j,end="")
    print()

for z in range(len(data)):
    printImg(image)
    for y in range(len(data[z])):
        for x in range(len(data[z][y])):
            if image[y][x] == 2:
                image[y][x] = data[z][y][x]


print(len(data))
