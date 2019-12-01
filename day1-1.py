from __future__ import print_function
# aoc 2019 day 1 problem 1
# read the file of module weights, and calculate the total fuel required
# 1/3 of weight (rounded down), minus 2

file = open("day1-1.txt","r")
t = 0
for n in file:
  w = int(n)
  f = (w // 3) - 2
  t += f
  print(w, f)

print("total",t)
file.close()

