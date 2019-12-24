from __future__ import print_function
class IntCode():
    'aoc 2019 integer code program interpreter'
    def __init__(self, mem = [], debug = False):
        self.debug = debug
        self.originalMem = mem[:]
        self.reset()
    def reset(self):
        self.pc = 0
        self.relativeOffset = 0 # day 9
        self.mem = self.originalMem[:]
        self.extramem = {}
        self.dataIn = []
        self.dataOut = []
        # 0 for reset, 3 for input, 99 for halt
        self.state = 0
    def addInput(self, newData):
        self.dataIn.append(newData)
        if self.state == 3:
            self.state = 0
    def getOutput(self):
        if len(self.dataOut) > 0:
            if self.state == 4:
                self.state = 0
            return self.dataOut.pop(0)
    def printOp(self, length):
        print(self.pc,":",end="")
        for j in range(length):
            print(self.readmem(self.pc+j),end=" ")
        print("[%d]" % self.relativeOffset)
    def readmem(self, location):
        if location >= 0 and location < len(self.mem):
            return self.mem[location]
        elif location in self.extramem:
            return(self.extramem[location])
        else:
            if self.debug:
                print("New memory read:",location)
            return 0
    def writemem(self, location, value):
        if location >= 0 and location < len(self.mem):
            self.mem[location] = value
        elif location > 0:
            if self.debug:
                if not location in self.extramem:
                    print("New memory write:",location)
            self.extramem[location] = value
    def doStep(self):
        op = self.mem[self.pc]
        fi = self.readmem(self.pc+1)
        fiData = fi
        fiMode = op // 100 % 10
        if fiMode == 0:
            fiData = self.readmem(fi)
        elif fiMode == 2:
            fi += self.relativeOffset
            fiData = self.readmem(fi)
        if (op % 100) in (1,2,5,6,7,8):
            se = self.readmem(self.pc+2)
            seData = se
            seMode = op // 1000 % 10
            if seMode == 0:
                seData = self.readmem(se)
            elif seMode == 2:
                se += self.relativeOffset
                seData = self.readmem(se)
        if (op % 100) in (1,2,7,8):
            ne = self.readmem(self.pc+3)
            #neData = ne
            neMode = op // 10000 % 10
            if neMode == 0:
                pass
                #neData = self.readmem(ne)
            elif neMode == 2:
                ne += self.relativeOffset
                #neData = self.readmem(ne)
        op = op % 100
        if op == 1:
            if self.debug:
                self.printOp(4)
                print("  %d = %d + %d" % (ne, fiData, seData))
            result = fiData + seData
            self.writemem(ne, result)
            self.pc += 4
        elif op == 2:
            if self.debug:
                self.printOp(4)
                print("  %d = %d * %d" % (ne, fiData, seData))
            result = fiData * seData
            self.writemem(ne, result)
            self.pc += 4
        elif op == 3:
            if self.debug:
                self.printOp(2)
                print("  input %d" % (fi))
            if len(self.dataIn) == 0:
                # suspend on no data available
                self.state = 3
                return
            result = self.dataIn.pop(0)
            self.writemem(fi, result)
            self.pc += 2
        elif op == 4:
            if self.debug:
                self.printOp(2)
                print("  output %d [%d]" % (fi, fiData))
            self.dataOut.append(fiData)
            self.pc += 2
            self.state = 4
            return
        elif op == 5:
            if self.debug:
                self.printOp(3)
                print("  if %d != 0 then %d" % (fiData, seData))
            if fiData != 0:
                self.pc = seData
            else:
                self.pc += 3
        elif op == 6:
            if self.debug:
                self.printOp(3)
                print("  if %d == 0 then %d" % (fiData, seData))
            if fiData == 0:
                self.pc = seData
            else:
                self.pc += 3
        elif op == 7:
            if self.debug:
                self.printOp(4)
                print("  %d = (%d < %d ? 1, 0)" % (ne, fiData, seData))
            if fiData < seData:
                self.writemem(ne, 1)
            else:
                self.writemem(ne, 0)
            self.pc += 4
        elif op == 8:
            if self.debug:
                self.printOp(4)
                print("  %d = (%d < %d ? 1, 0)" % (ne, fiData, seData))
            if fiData == seData:
                self.writemem(ne, 1)
            else:
                self.writemem(ne, 0)
            self.pc += 4
        elif op == 9:
            if self.debug:
                self.printOp(2)
                print("  offset += %d" % (fiData))
            self.relativeOffset += fiData
            self.pc += 2
        elif op == 99:
            if self.debug:
                self.printOp(1)
                print("  halt")
            self.state = 99
        else:
            self.printOp(4)
            print("Instruction error at",self.pc)
            self.state = 99
    def doRunInteractive(self):
        while self.state == 0:
            self.doStep()
            if self.state == 3:
                data = int(raw_input("?"))
                self.addInput(data)
            if self.state == 4:
                print(self.getOutput())
    def doRun(self):
        while self.state == 0:
            self.doStep()
