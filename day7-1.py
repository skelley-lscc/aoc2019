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

def initExec(mem, dataIn=[], debug = False):
    # execute memory array program
    # 1 for add, 2 for multiply, 99 to stop
    # 1 a b c is [c] = [a] + [b]
    # 2 d e f is [d] = [e] * [f]
    # 3 a is input, store at a
    # 4 b is output, store at b
    # 99 is stop
    pc = 0
    dataOut = []
    op = mem[pc] % 100
    while op != 99:
        if debug: print("op=",op)
        if op == 1:
            fi = mem[pc+1]
            se = mem[pc+2]
            ne = mem[pc+3]
            if debug: print("%d: [%d] = [%d] + [%d]" % (pc,ne,fi,se))
            if mem[pc] // 100 % 10 == 0:
                fi = mem[fi]
            if mem[pc] // 1000 % 10 == 0:
                se = mem[se]
            result = fi + se
            if debug: print("    %d = %d + %d" % (result,mem[fi],mem[se]))
            mem[ne] = result
            pc += 4
        elif op == 2:
            fi = mem[pc+1]
            se = mem[pc+2]
            ne = mem[pc+3]
            if debug: print("%d: [%d] = [%d] * [%d]" % (op,ne,fi,se))
            if mem[pc] // 100 % 10 == 0:
                fi = mem[fi]
            if mem[pc] // 1000 % 10 == 0:
                se = mem[se]
            result = fi * se
            if debug: print("    %d = %d * %d" % (result,mem[fi],mem[se]))
            mem[ne] = result
            pc += 4
        elif op == 3:   # input
            fi = mem[pc+1]
            if len(dataIn) > 0:
                se = dataIn.pop(0)
                if debug: print("using",se,"from input")
            else:
                se = int(input("?"))
            mem[fi] = se
            pc += 2
        elif op == 4:   # output
            fi = mem[pc+1]
            if mem[pc] // 100 % 10 == 0:
                fi = mem[fi]
            if debug: print("output",mem[pc+1],":",fi)
            dataOut.append(fi)
            pc += 2
        elif op == 5: # jump if true
            fi = mem[pc+1]
            se = mem[pc+2]
            if mem[pc] // 100 % 10 == 0:
                fi = mem[fi]
            if mem[pc] // 1000 % 10 == 0:
                se = mem[se]
            if fi != 0:
                pc = se
            else:
                pc += 3
        elif op == 6: # jump if false
            fi = mem[pc+1]
            se = mem[pc+2]
            if mem[pc] // 100 % 10 == 0:
                fi = mem[fi]
            if mem[pc] // 1000 % 10 == 0:
                se = mem[se]
            if fi == 0:
                pc = se
            else:
                pc += 3
        elif op == 7: # fi less than se, store 1
            fi = mem[pc+1]
            se = mem[pc+2]
            ne = mem[pc+3]
            if debug: print("%d: [%d] = [%d] < [%d]" % (op,ne,fi,se))
            if mem[pc] // 100 % 10 == 0:
                fi = mem[fi]
            if mem[pc] // 1000 % 10 == 0:
                se = mem[se]
            if debug: print("    %d = %d < %d" % (result,fi,se))
            if fi < se:
                mem[ne] = 1
            else:
                mem[ne] = 0
            pc += 4
        elif op == 8: # fi equals se, store 1
            fi = mem[pc+1]
            se = mem[pc+2]
            ne = mem[pc+3]
            if debug: print("%d: [%d] = [%d] < [%d]" % (op,ne,fi,se))
            if mem[pc] // 100 % 10 == 0:
                fi = mem[fi]
            if mem[pc] // 1000 % 10 == 0:
                se = mem[se]
            if debug: print("    %d = %d < %d" % (result,fi,se))
            if fi == se:
                mem[ne] = 1
            else:
                mem[ne] = 0
            pc += 4
        else:
            print("instruction error at",pc)
            break
        op = mem[pc] % 100
    if op != 99:
        print("abnormal end",op)
    return(dataOut)

results = []
def thrusters(used, mem, data, debug=False):
    global results
    if len(used) == 5:
        print(used, data)
        results.append((used[:],data))
        return
    for x in range(0,5):
        if x not in used:
            used.append(x)
            input = [x, data]
            if debug: print("executing",used, input)
            dataOut = initExec(mem[:], input)
            if debug: print("calling",used, dataOut)
            thrusters(used, mem, dataOut[0])
            if debug: print("finished",used, dataOut)
            used.remove(x)

xmem = readData("day7-1.txt")
#xmem = readData("day7-tiny.txt")
mem = xmem[:]
#print(mem)
#o = initExec(mem,[1,0])
#print(o)
thrusters([], mem, 0)
largest = 0
order = []
for r in results:
    if r[1] > largest:
        largest = r[1]
        order = r[0]
print("largest is", largest, order)
