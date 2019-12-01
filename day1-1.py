from __future__ import print_function
file = open("day1-1.txt","r")
t = 0
for n in file:
  w = int(n)
  f = (w // 3) - 2
  t += f
  print(w, f)

print("total",t)
file.close()

