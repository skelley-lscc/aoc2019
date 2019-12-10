from __future__ import print_function
from IntCode import IntCode

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

mem = readData("day9-1.txt")
#mem = xmem[:]
#mem = parseLine("109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99")

print(mem)
machine = IntCode(mem, False)
machine.doRunInteractive()
