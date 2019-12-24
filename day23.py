# day 23 network simulation
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

mem = readData("day23.txt")
#print(mem)
partTwo = True
# start the game for part 2

machines = []
queue = {}
partial = {}
idle = []           # part 2
NATx = 0; NATy = 0  # part 2
NATyHistory = []    # part 2
for _ in range(50):
    machines.append(IntCode(mem, False))
    queue[_] = [_]  # first input is machine #
    partial[_] = []
    idle.append(0)  # part 2

while True:
    for m in range(len(machines)):
        machine = machines[m]
        if machine.state != 99:
            machine.doStep()
        if machine.state == 3:
        # feed a network packet to this machine, or -1
            if len(queue[m]) > 0:
                idle[m] = 0     # part 2
                machine.addInput(queue[m].pop(0))
            else:
                idle[m] += 1    # part 2
                machine.addInput(-1)
        if machine.state == 4:
        # add a network packet to the queue of another machine
            data = machine.getOutput()
            partial[m].append(data)
            if len(partial[m]) == 3:
                dest = partial[m][0]
                x = partial[m][1]
                y = partial[m][2]
                print(dest,x,y, end="; ")
                if not dest in queue:
                    print("new dest",dest)
                    queue[dest] = []
                queue[dest].append(x)
                queue[dest].append(y)
                partial[m].pop(0)
        if 255 in queue and len(queue[255]) == 2:
            print("255: ",queue[255])
            #z = raw_input("That's all for part 1")
            NATx = queue[255].pop(0)
            NATy = queue[255].pop(0)
            queue[255] = []
        if min(idle) > 3:
            print("Injecting...")
            # send the packet to 0, reset idle counter
            for i in range(50):
                idle[i] = 0
            queue[0].append(NATx)
            queue[0].append(NATy)
            if NATy in NATyHistory:
                print("Second Y is",NATy)
                zz = raw_input("Done?")
            NATyHistory.append(NATy)
