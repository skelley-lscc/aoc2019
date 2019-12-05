low = 387638
high = 919123
count = 0
part1 = False

for i in range(low,high):
    counts = [0] * 10
    s = "000000" + str(i)
    s = s[-6:]
    double = False
    ascend = True
    for j in range(5):
        counts[int(s[j])] += 1
        if s[j] == s[j+1]:
            double = True
        if s[j] > s[j+1]:
            ascend = False
    counts[int(s[5])] += 1
    if double and ascend and (part1 or 2 in counts):
        print s, counts
        count += 1
print count
