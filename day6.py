from __future__ import print_function
from anytree import Node, RenderTree, Walker

# part one is a simple depth measurement for each node

def readData(filename):
    debug = False
    # read input file, build memory tree
    data = {}
    # input file is out of order
    f = open(filename,"r")
    line = f.readline().strip()
    while len(line) > 0:
        orbit = line.split(")")
        data[orbit[1]] = orbit[0]
        line = f.readline().strip()
    f.close()
    if debug: print(data)
    
    # now fix the parents
    # this hurts -- make a Node, add it to the nodes dict
    # and remove the node data from the data list
    root = Node("COM")
    nodes = {}
    nodes[root.name] = root
    while len(data) > 0:
        if debug: print(len(data))
        popList = []
        for (d,p) in data.iteritems():
            # if we have added the parent to the tree
            if p in nodes:
                if debug: print(d,p)
                next = Node(d, parent=nodes[p])
                popList.append(d)
                nodes[d] = next
        # cannot remove nodes from dict while looping over it
        for po in popList:
            data.pop(po)
    return nodes

#orbitDict = readData("day6-tiny.txt")
orbitDict = readData("day6-1.txt")
orbits = orbitDict["COM"]
#print(RenderTree(orbits))

total = 0
for pre, _, node in RenderTree(orbits):
    total += len(node.path) - 1
print("Total orbits is:",total)

w = Walker()
#xfer = w.walk(orbitDict["L"],orbitDict["H"])
xfer = w.walk(orbitDict["YOU"],orbitDict["SAN"])

#print(xfer)
#print(xfer[0])
#print(xfer[1])
#print(xfer[2])

count = 0
for _ in xfer[0]:
    print(_)
    count += 1
try:
    for _ in xfer[1]:
        count += 1
except TypeError:
    print("Error in xfer[1]: ",xfer[1])
    count += 1
for _ in xfer[2]:
    print(_)
    count += 1
print("Length of path (including ends) is",count)
print("Subtract 3 for the puzzle answer")

