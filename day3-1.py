from __future__ import print_function

def readData(filename):
    # read input file, build memory array
    wires = []
    f = open(filename,"r")
    data = f.readline()
    while len(data) > 0:
        wire = data.split(",")
        segment = []
        old = (0,0)
        segment.append(old)
        for item in wire:
            dir = item[0]
            size = int(item[1:])
            if dir == "U":
                new = (old[0],old[1]+size)
            elif dir == "D":
                new = (old[0],old[1]-size)
            elif dir == "L":
                new = (old[0]-size,old[1])
            elif dir == "R":
                new = (old[0]+size,old[1])
            else:
                print("error in line input:",item)
                break
            segment.append(new)
            old = new
        wires.append(segment)
        data = f.readline()
    f.close()
    return wires

def interse(p1,p2,q1,q2):
    inter = (0,0)
    print("--",p1,p2,q1,q2)
    if p1[0] == p2[0]:
        s = p1[0]
        if q1[0] < s and q2[0] > s or q1[0] > s and q2[0] < s:
            t = q1[1]
            print("****")
            if p1[1] < t and p2[1] > t or p1[1] > t and p2[1] < t:
                print("*******")
                print("(",s,",",t,")")
                inter = (s,t)
    elif p1[1] == p2[1]:
        s = p1[1]
        if q1[1] < s and q2[1] > s or q1[1] > s and q2[1] < s:
            t = q1[0]
            print("++++")
            if p1[0] < t and p2[0] > t or p1[0] > t and p2[0] < t:
                print("*******")
                print("(",s,",",t,")")
                inter = (s,t)
    return inter

#wires = readData("day3-tiny.txt")
wires = readData("day3-1.txt")
print(wires)
intersect ={}
while len(wires) > 1:
    x = wires.pop()
    old = x.pop()
    while len(x) > 0:
        new = x.pop()
        for w in wires:
            for j in range(len(w)-1):
                z = interse(old,new,w[j],w[j+1])
                g = abs(z[0])+abs(z[1])
                if g > 0 and not g in intersect:
                    intersect[g] = z
                elif g > 0:
                    print("duplicate distance",z)
        old = new
print(intersect)
small = []
for i in intersect:
    small.append(i)
small.sort()
print(small[0],intersect[small[0]])
