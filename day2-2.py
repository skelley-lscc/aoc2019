from __future__ import print_function

def readData(filename):
    # read input file, build memory array
    xmem = []
    f = open(filename,"r")
    data = f.readline()
    while len(data) > 0:
        line = data.split(",")
        for item in line:
            xmem.append(int(item))
        data = f.readline()
    f.close()
    return xmem

def initExec(mem, debug = False):
    # execute memory array program
    # 1 for add, 2 for multiply, 99 to stop
    # 1 a b c is [c] = [a] + [b]
    # 2 d e f is [d] = [e] * [f]
    # 99 is stop
    pc = 0
    op = mem[pc]
    while op in (1,2):
        if op == 1:
            fi = mem[pc+1]
            se = mem[pc+2]
            ne = mem[pc+3]
            if debug: print("%d: [%d] = [%d] + [%d]" % (pc,ne,fi,se))
            result = mem[fi] + mem[se]
            if debug: print("    %d = %d + %d" % (result,mem[fi],mem[se]))
            mem[ne] = result
            pc += 4
        elif op == 2:
            fi = mem[pc+1]
            se = mem[pc+2]
            ne = mem[pc+3]
            if debug: print("%d: [%d] = [%d] * [%d]" % (op,ne,fi,se))
            result = mem[fi] * mem[se]
            if debug: print("    %d = %d * %d" % (result,mem[fi],mem[se]))
            mem[ne] = result
            pc += 4
        else:
            print("instruction error at",pc)
            break
        op = mem[pc]

xmem = readData("day2-1.txt")
m1 = 0
m2 = 0
search = True
while search:
    mem = xmem[:]
    mem[1] = m1
    mem[2] = m2
    initExec(mem)
    if mem[0] != 19690720:
        m2 += 1
        if m2 > 100:
            m2 = 0
            m1 += 1
            if m1 > 100:
                print("did not find it")
                search = False
    else:
        search = False
print("finish",m1,m2)
