from __future__ import print_function
# aoc 2019 day 1 part 2
# same calculation, but rocket fuel required fuel, too

file = open("day1-1.txt","r")
t = 0
for n in file:
  w = int(n)
  while w > 0:
    f = (w // 3) - 2
    if (f < 0):
      f = 0
    t += f
    w = f
  print(w, f)

print("total",t)
file.close()

