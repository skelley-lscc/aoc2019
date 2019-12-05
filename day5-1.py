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
    # 3 a is input, store at a
    # 4 b is output, store at b
    # 99 is stop
    pc = 0
    op = mem[pc] % 100
    while op != 99:
        print(op)
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
            se = int(input("?"))
            mem[fi] = se
            pc += 2
        elif op == 4:   # output
            fi = mem[pc+1]
            if mem[pc] // 100 % 10 == 0:
                fi = mem[fi]
            print("output",mem[pc+1],":",fi)
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

xmem = readData("day5-1.txt")
mem = xmem[:]
print(mem)
initExec(mem)

