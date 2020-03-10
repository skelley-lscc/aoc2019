from __future__ import print_function
from IntCode import IntCode
# day 15 -- blind maze
# north 1, south 2, west 3, east 4

class Robot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.dx = 0
        self.dy = -1
        self.hull = {}
        self.hull[(self.x,self.y)] = "."
        self.found = False
        self.newSquareCount = 0
        self.state = 0  # 0 search, 1 mapping
        self.moveQueue = []
        self.requestedDir = 0
    def getNextMove(self):
        # is there unexplored next to our current position?
        if self.state == 0:
            if len(self.moveQueue) == 0:
                if (self.x-1,self.y) not in self.hull:
                    self.moveQueue.append(1)
                elif (self.x+1,self.y) not in self.hull:
                    self.moveQueue.append(2)
                elif (self.x,self.y-1) not in self.hull:
                    self.moveQueue.append(3)
                elif (self.x,self.y+1) not in self.hull:
                    self.moveQueue.append(4)
        if len(self.moveQueue) > 0:
            next = self.moveQueue.pop()
        else:
            next = 0; self.found = True # not really
        self.requestedDir = next
        return next
    def moveResult(self, result):
        if result == 2: self.found = True
        # calculate where our new position would be
        newX = self.x; newY = self.y
        if self.requestedDir == 1: newX-=1
        if self.requestedDir == 2: newX+=1
        if self.requestedDir == 3: newY-=1
        if self.requestedDir == 4: newY+=1
        # store the result of our attempted move
        self.hull[(newX,newY)] = result
        if self.state == 0:
            # search mode, return to position
            pass
        if result > 0:
            # not a wall, update our position
            self.x = newX; self.y = newY
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
        print(sizeX, sizeY, minX, minY)
        hull = []
        for h in range(sizeY):
            hull.append([' '] * sizeX)
        for p in self.hull:
            spot = ' '
            if self.hull[p] == 2: spot = '!'
            if self.hull[p] == 1: spot = '.'
            if self.hull[p] == 0: spot = '#'
            if p[0] == 0 and p[1] == 0: spot = '%'
            try:
                hull[p[1]-minY][p[0]-minX] = spot
            except:
                print(p, self.hull[p])
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

mem = readData("day15.txt")
print(mem)
machine = IntCode(mem, False)
robot = Robot()
partTwo = False
if partTwo: robot.hull[(0,0)] = 1

while  machine.state != 99 and robot.found == False:
    machine.doRun()
    if machine.state == 3:
        machine.addInput(robot.getNextMove())
    if machine.state == 4:
        color = machine.getOutput()
        robot.moveResult(color)
        machine.doRun()
print(robot.hull)
robot.printHull()
