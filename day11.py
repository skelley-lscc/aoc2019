from __future__ import print_function
from IntCode import IntCode
# set partTwo to True or False to start the robot
# on a black or white square

class Robot():
    # hull 0 is black, 1 is white (default black)
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.dx = 0
        self.dy = -1
        self.hull = {}
        self.newSquareCount = 0
    def paint(self, color):
        if (self.x,self.y) not in self.hull:
            self.newSquareCount += 1
        self.hull[(self.x,self.y)] = color
    def turnAndMove(self, direction):
        # 0 for ccw, 1 for cw
        if direction == 0:
            self.dir = (self.dir + 270) % 360
        elif direction == 1:
            self.dir = (self.dir + 90) % 360
        if self.dir == 0:
            self.dx = 0; self.dy = -1
        elif self.dir == 90:
            self.dx = 1; self.dy = 0
        elif self.dir == 180:
            self.dx = 0; self.dy = 1
        elif self.dir == 270:
            self.dx = -1; self.dy = 0
        # now move one square
        self.x += self.dx; self.y += self.dy
    def getColor(self):
        if (self.x,self.y) in self.hull:
            return self.hull[(self.x,self.y)]
        return 0
    def printHull(self):
        maxX = 0; maxY = 0
        minX = 0; minY = 0
        for p in self.hull:
            if p[0] > maxX:
                maxX = p[0]
            elif p[0] < minX:
                minX = p[0]
            if p[1] > maxY:
                maxY = p[1]
            elif p[1] < minY:
                minY = p[1]
        maxX += 1; maxY += 1
        sizeX = maxX - minX; sizeY = maxY - minY
        print(sizeX, sizeY)
        hull = []
        for h in range(sizeY):
            hull.append(['.'] * sizeX)
        for p in self.hull:
            if self.hull[p] == 1:
                try:
                    hull[p[1]-minY][p[0]-minX] = '#'
                except:
                    print(p)
        for line in hull:
            for c in line:
                print(c, end='')
            print()

def parseLine(data):
    xmem = []
    line = data.split(",")
    for item in line:
        xmem.append(int(item))
    return xmem

def readData(filename):
    # read input file, build memory array
    xmem = []
    f = open(filename,"r")
    data = f.readline()
    while len(data) > 0:
        newmem = parseLine(data)
        for i in newmem:
            xmem.append(i)
        data = f.readline()
    f.close()
    return xmem

mem = readData("day11-1.txt")
print(mem)
machine = IntCode(mem, True)
robot = Robot()
# For part 2, start on a white square
partTwo = True
if partTwo: robot.hull[(0,0)] = 1

while  machine.state != 99:
    machine.doRun()
    if machine.state == 3:
        machine.addInput(robot.getColor())
    if machine.state == 4:
        color = machine.getOutput()
        robot.paint(color)
        machine.doRun()
        direction = machine.getOutput()
        print(color, direction)
        robot.turnAndMove(direction)
print("Squares painted:", robot.newSquareCount)
print(robot.hull)
robot.printHull()
