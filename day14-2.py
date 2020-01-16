from __future__ import print_function

# part one is calculate how many ore is needed for one fuel
# part two is how many fuel for 1 trillion ore
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
fuel = stepDict["FUEL"]
# to make a fuel, the ingredients need to be made
# loop all the way back to ORE
print(stepDict)
print(fuel)     # uses REPR
# keep up with the extra generated, use as we can
extra = {}
makemore = True
oreOnHand = 1000000000000
fuelCount = 0
while makemore:
    needs = {}
    for t in fuel.requires:
        #print(t)    # this is ['4', 'ITEM']
        needs[t[1]] = int(t[0])
    #print(needs)
    while len(needs) > 1:
        #print(needs)
        # make a list of the next items to process
        next = []
        for item in needs:
            if item != 'ORE':
                next.append(item)
        #print(next)
        # pop each need, and add a multiple of the ingredients back to needs
        for item in next:
            qtyNeeded = int(needs.pop(item))
            if item in extra:
                overage = extra[item]
                if qtyNeeded < overage:
                    #print("-- used",qtyNeeded,"overage of",item,overage-qtyNeeded,"left")
                    extra[item] = overage - qtyNeeded
                    qtyNeeded = 0
                else:
                    qtyNeeded -= overage
                    #print("-- used",overage,"overage of",item,"still need",qtyNeeded)
                    extra.pop(item)
            reqs = stepDict[item]
            #print(reqs)
            qtyProvided = int(reqs.product[0])
            multiple = int(qtyNeeded / qtyProvided)
            if multiple * qtyProvided < qtyNeeded:
                # make an additional one
                multiple += 1
                # add to extra production
                prevExtra = 0
                if item in extra:
                    prevExtra = extra[item]
                extra[item] = (multiple * qtyProvided) - qtyNeeded
                #print("-- now have",extra[item],"extra of",item)
            #print(qtyNeeded, qtyProvided, multiple)
            for ingredient in reqs.requires:
                prevQty = 0
                if ingredient[1] in needs:
                    prevQty = needs[ingredient[1]]
                    #print("-- already needed",prevQty,ingredient[1])
                needs[ingredient[1]] = prevQty + int(ingredient[0]) * multiple
                #print("- add ",needs[ingredient[1]], " ", ingredient[1])
    oreNeeded = int(needs['ORE'])
    #print(oreNeeded)
    if oreNeeded > oreOnHand:
        makemore = False
    else:
        oreOnHand -= oreNeeded
        fuelCount += 1
        if fuelCount % 1000 == 0:
            print(fuelCount,"fuel",oreOnHand,"ore left")
print(fuelCount,"fuel")
