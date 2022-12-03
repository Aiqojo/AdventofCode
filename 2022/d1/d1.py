import os

p = []
f = open("t1.txt", "r")

for line in f:
    p.append(line.strip())

mx = [0, 0, 0]
cur = 0
indx = 0
for line in p:
    if line == "":
        if min(mx) < cur:
            mx[mx.index(min(mx))] = cur
        indx += 1
        cur = 0
    else:
        cur += int(line)

print("part 1: ", max(mx))
print("part 2:", sum(mx))
