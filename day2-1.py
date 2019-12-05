from __future__ import print_function

# read input file, build memory array
mem = []
f = open("day2-1.txt","r")
data = f.readline()
while len(data) > 0:
    line = data.split(",")
    for item in line:
        mem.append(int(item))
    print(line)
    print(mem)
    data = f.readline()
f.close()

# replacement values
mem[1] = 12
mem[2] = 2

# execute memory array program
# 1 for add, 2 for multiply, 99 to stop
# 1 a b c is [c] = [a] + [b]
# 2 d e f is [d] = [e] * [f]
# 99 is stop

op = 0
while mem[op] in (1,2):
    fi = mem[op+1]
    se = mem[op+2]
    ne = mem[op+3]
    if mem[op] == 1:
        print("%d: [%d] = [%d] + [%d]" % (op,ne,fi,se))
        result = mem[fi] + mem[se]
        print("    %d = %d + %d" % (result,mem[fi],mem[se]))
        mem[ne] = result
    if mem[op] == 2:
        print("%d: [%d] = [%d] * [%d]" % (op,ne,fi,se))
        result = mem[fi] * mem[se]
        print("    %d = %d * %d" % (result,mem[fi],mem[se]))
        mem[ne] = result
    op += 4

print("finish",mem[0])
