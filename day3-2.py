from __future__ import print_function

def readData(filename):
    # read input file, build memory array
    wires = []
    f = open(filename,"r")
    data = f.readline()
    while len(data) > 0:
        wire = data.split(",")
        segment = []
        length = 0
        old = (0,0,0)
        segment.append(old)
        for item in wire:
            dir = item[0]
            size = int(item[1:])
            length += size
            if dir == "U":
                new = (old[0],old[1]+size,length)
            elif dir == "D":
                new = (old[0],old[1]-size,length)
            elif dir == "L":
                new = (old[0]-size,old[1],length)
            elif dir == "R":
                new = (old[0]+size,old[1],length)
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
    inter = (0,0,0)
    #print("--",p1,p2,q1,q2)
    if p1[0] == p2[0]:
        s = p1[0]
        if q1[0] < s and q2[0] > s or q1[0] > s and q2[0] < s:
            t = q1[1]
            #print("****")
            if p1[1] < t and p2[1] > t or p1[1] > t and p2[1] < t:
                print("*******")
                #print("(",s,",",t,")")
                sum = min(p1[2],p2[2])+min(q1[2],q2[2])
                if p1[2] < p2[2]:
                    sum += abs(p1[1]-t)
                else:
                    sum += abs(p2[1]-t)
                if q1[2] < q2[2]:
                    sum += abs(q1[0]-s)
                else:
                    sum += abs(q2[0]-s)
                inter = (s,t,sum)
                print(inter)
                print(p1,p2)
                print(q1,q2)
    elif p1[1] == p2[1]:
        s = p1[1]
        if q1[1] < s and q2[1] > s or q1[1] > s and q2[1] < s:
            t = q1[0]
            #print("++++")
            if p1[0] < t and p2[0] > t or p1[0] > t and p2[0] < t:
                print("+++++++")
                #print("(",s,",",t,")")
                sum = min(p1[2],p2[2])+min(q1[2],q2[2])
                if p1[2] < p2[2]:
                    sum += abs(p1[0]-t)
                else:
                    sum += abs(p2[0]-t)
                if q1[2] < q2[2]:
                    sum += abs(q1[1]-s)
                else:
                    sum += abs(q2[1]-s)
                inter = (s,t,sum)
                print(inter)
                print(p1,p2)
                print(q1,q2)
    return inter

#wires = readData("day3-tiny.txt")
#wires = readData("day3-610step.txt")
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
                #g = abs(z[0])+abs(z[1])
                g = z[2]
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
