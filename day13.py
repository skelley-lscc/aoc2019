# day 13 breakout game
from __future__ import print_function
from IntCode import IntCode

class Robot():
    # hull 0 is black, 1 is white (default black)
    def __init__(self):
        self.board = {}
        self.newItemCount = 0
        self.score = 0  # part 2
        self.ballX = 0  # part 2
        self.ballY = 0  # part 2
        self.ballDX = 0     # part 2
        self.paddleX = 0    # part 2
    def plot(self, x, y, item):
        if (x,y) not in self.board:
            self.newItemCount += 1
        self.board[(x,y)] = item
    def getItem(self, x, y):
        if (x, y) in self.board:
            return self.board[(x,y)]
        return 0
    def printBoard(self):
        self.blockCount = 0
        maxX = 0; maxY = 0
        minX = 0; minY = 0
        for p in self.board:
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
        #print(sizeX, sizeY)
        board = []
        for h in range(sizeY):
            board.append([' '] * sizeX)
        for p in self.board:
            item = self.board[p]
            if p[0] == -1:  # part 2 -- score
                self.score = item
            elif item == 0: # empty
                itemC = ' '
            elif item == 1: # wall
                itemC = '#'
            elif item == 2: # block
                self.blockCount += 1
                itemC = '~'
            elif item == 3: # paddle
                itemC = '='
                self.paddleX = p[0]
            elif item == 4: # ball
                if p[0] < self.ballX:
                    self.ballDX = -1
                else:
                    self.ballDX = 1
                self.ballX = p[0]
                self.ballY = p[1]
                itemC = '@'
            if item >= 0:
                board[p[1]-minY][p[0]-minX] = itemC
        for line in board:
            for c in line:
                print(c, end='')
            print()
        print("Score:", self.score)

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

mem = readData("day13-1.txt")
print(mem)
partTwo = True
# start the game for part 2
if partTwo:
    mem[0] = 2
machine = IntCode(mem, False)
robot = Robot()

while machine.state != 99:
    machine.doRun()
    if machine.state == 3:
        robot.printBoard()
        # joystick input: -1 left, 0 neutral, 1 right
        px = robot.paddleX; bx = robot.ballX; dx = robot.ballDX
        print(px,bx,dx,robot.ballY)
        newBallX = bx+(22-robot.ballY)*dx
        print(newBallX)
        if px == newBallX:
            machine.addInput(0)
        elif px > newBallX:
            machine.addInput(-1)
        elif px < newBallX:
            machine.addInput(1)
        else:
            machine.addInput(0)
    if machine.state == 4:
        x = machine.getOutput()
        machine.doRun()
        y = machine.getOutput()
        machine.doRun()
        item = machine.getOutput()
        robot.plot(x,y,item)
print("Game Over")
robot.printBoard()
print("Block count is", robot.blockCount)
