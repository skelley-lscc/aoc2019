from __future__ import print_function

SIZE = 119315717514047
deck = [0] * SIZE
for _ in range(SIZE):
    deck[_] = _

print(deck)

def reverse(deck):
    new = deck[:]
    new.reverse()
    return new

def cut(deck, N):
    if N > 0:
        new = deck[N:]
        for d in deck[:N]:
            new.append(d)
    else:
        new = deck[N:]
        for d in deck[:N]:
            new.append(d)
    return new

def deal(deck, increment):
    new = [0] * len(deck)
    next = 0; count = 0
    while count < len(deck):
        new[next] = deck[count]
        count += 1; next += increment
        next = next % len(deck)
    return new

for i in range(101741582076661):
    f = open("day22.txt","r")
    # can't strip the spaces
    line = f.readline().strip()
    while len(line) > 0:
        words = line.split()
        if words[0] == "cut":
            deck = cut(deck, int(words[1]))
        if words[1] == "into":
            deck = reverse(deck)
        if words[1] == "with":
            deck = deal(deck, int(words[3]))
        line = f.readline().strip()
    f.close()
    if i % 100000000 == 0:
        print(i)
print(deck)
# what is in position 2020?
print(deck[2020])
# where is card 2019?
for i in range(len(deck)):
    if deck[i] == 2019:
        print("position", i)
