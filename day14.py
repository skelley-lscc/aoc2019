from __future__ import print_function

# part one is calculate how many ore is needed for one fuel
class Step(object):
    def __init__(self, product, requires):
    # product is (name, qty); requires is [(name, qty),...]
        self.name = product[1]
        self.product = product
        self.requires = requires
    def __repr__(self):
        s = ""
        for r in self.requires:
            s += r[0] + " " + r[1] + ","
        s = s[:-1] + " => "
        s += self.product[0] + " " + self.product[1]
        return s

def readData(filename):
    debug = False
    # read input file, build memory tree
    data = {}
    # input file is out of order
    f = open(filename,"r")
    line = f.readline().strip()
    while len(line) > 0:
        reaction = line.split("=>")
        needs = reaction[0].split(",")
        product = reaction[1].strip().split(" ")
        requires = []
        for n in needs:
            requires.append(n.strip().split(" "))
        step = Step(product, requires)
        data[step.name] = step
        line = f.readline().strip()
    f.close()
    if debug: print(data)
    return data

stepDict = readData("day14-1.txt")
top = stepDict["FUEL"]
print(stepDict)
