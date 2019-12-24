from __future__ import print_function
#<x=17, y=-12, z=13>
#<x=2, y=1, z=1>
#<x=-1, y=-17, z=7>
#<x=12, y=-14, z=18>

class Planet():
    def __init__(self, px, py, pz):
        self.tick = 0
        self.history = {}
        self.ix = px; self.x = px
        self.iy = py; self.y = py
        self.iz = pz; self.z = pz
        self.vx = 0
        self.vy = 0
        self.vz = 0
    def __str__(self):
        return str(self.x)+","+str(self.y)+","+str(self.z)+":"+str(self.vx)+","+str(self.vy)+","+str(self.vz)
    def addGravity(self, otherP):
        if self.x > otherP.x:
            self.vx -= 1
            otherP.vx += 1
        elif self.x < otherP.x:
            self.vx += 1
            otherP.vx -= 1
        if self.y > otherP.y:
            self.vy -= 1
            otherP.vy += 1
        elif self.y < otherP.y:
            self.vy += 1
            otherP.vy -= 1
        if self.z > otherP.z:
            self.vz -= 1
            otherP.vz += 1
        elif self.z < otherP.z:
            self.vz += 1
            otherP.vz -= 1
    def addVelocity(self):
        # add to history before modifying
        #newPos = (self.x, self.y, self.z)
        #if not newPos in self.history:
        #    self.history[newPos] = 1
        #else:
        #    self.history[newPos] += 1
        #    print(self,"repeats")
        self.tick += 1
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        # its repeats a previous state, not the initial state
        #if self.x == self.ix:
            #if self.y == self.iy:
            #    if self.z == self.iz:
            #        if self.repeats == 0:
            #            self.repeats = self.tick
            #            print(self,"repeats at",self.repeats)
    #def unique(self):
    #    return ((self.x,self.y,self.z) not in self.history)
    def atInitialX(self):
        return self.x == self.ix and self.vx == 0
    def atInitialY(self):
        return self.y == self.iy and self.vy == 0
    def atInitialZ(self):
        return self.z == self.iz and self.vz == 0
    def getEnergy(self):
        potentialE = abs(self.x) + abs(self.y) + abs(self.z)
        kineticE = abs(self.vx) + abs(self.vy) + abs(self.vz)
        energy = potentialE * kineticE
        return energy

def gcd(a,b):
    if a == 0 or b == 0:
        return abs(b-a)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

planets = []
# problem data part 1
p = Planet(17, -12, 13)
q = Planet(2, 1, 1)
r = Planet(-1, -17, 7)
s = Planet(12, -14, 18)
# tiny set 1
if False:
    p = Planet(-1, 0, 2)
    q = Planet(2, -10, -7)
    r = Planet(4, -8, 8)
    s = Planet(3, 5, -1)
# tiny set 2
if False:
    p = Planet(-8, -10, 0)
    q = Planet(5, 5, 10)
    r = Planet(2, -7, 3)
    s = Planet(9, -8, -3)
planets.append(p)
planets.append(q)
planets.append(r)
planets.append(s)

found = False; foundX = False; foundY = False; foundZ = False
repeatX = 0; repeatY = 0; repeatZ = 0
#while p.unique() or q.unique() or r.unique() or s.unique():
while not found:
    for i in range(len(planets)-1):
        for j in range(i+1, len(planets)):
            planets[i].addGravity(planets[j])
    for i in range(len(planets)):
        planets[i].addVelocity()
    thisX = True; thisY = True; thisZ = True
    for i in range(len(planets)):
        thisX = thisX and planets[i].atInitialX()
        thisY = thisY and planets[i].atInitialY()
        thisZ = thisZ and planets[i].atInitialZ()
    if thisX and not foundX:
        repeatX = p.tick
        print("X repeats at",repeatX)
        foundX = True
    if thisY and not foundY:
        repeatY = p.tick
        print("Y repeats at",repeatY)
        foundY = True
    if thisZ and not foundZ:
        repeatZ = p.tick
        print("Z repeats at",repeatZ)
        foundZ = True
    found = foundX and foundY and foundZ
        #if p.tick > 2770:
        #print(p.tick,p,q,r,s)
        #ee = raw_input("?")
    if p.tick % 1000000 == 1:
        print(p.tick)
    elif p.tick % 100000 == 1:
        print(p.tick,".",end="")
# part 1 is total energy after 1000
totEnergy = p.getEnergy()+q.getEnergy()+r.getEnergy()+s.getEnergy()
print(p.tick, totEnergy)
# part 2 is tick when the positions repeat
# calculate repeat of each x, y, z independently
# then take the LCM of the three
requiredCount = repeatX * repeatY * repeatZ
print(requiredCount)
print(gcd(repeatX,repeatY))
print(gcd(repeatX,repeatZ))
print(gcd(repeatY,repeatZ))
#requiredCount /= gcd(gcd(repeatX,repeatY),repeatZ)
requiredXY = (repeatX * repeatY) / gcd(repeatX,repeatY)
requiredCount = (requiredXY * requiredZ) / gcd(requiredXY,requiredZ)
print(requiredCount)
